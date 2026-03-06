#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 5 Full Pipeline Test Script (Production Ready)
功能：解析 JSON 日志，计算核心业务指标 (GMV, UV, 转化率, 品类排行)
数据源：data/*.log (JSON Lines 格式)
输出：output/ads_business_report.json & .txt
"""

import os
import sys
import json
import logging
from datetime import datetime
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BusinessETLPipeline:
    def __init__(self, base_dir=None):
        self.base_dir = base_dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(self.base_dir, "data")
        self.output_dir = os.path.join(self.base_dir, "output")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # 中间状态存储
        self.raw_count = 0
        self.error_count = 0
        self.records = []

    def extract_ods(self):
        """ODS 层：读取原始日志"""
        log_files = [f for f in os.listdir(self.data_dir) if f.endswith('.log')]
        if not log_files:
            raise FileNotFoundError("未找到 .log 数据文件")
        
        logger.info(f"📂 发现数据文件：{log_files}")
        
        for fname in log_files:
            fpath = os.path.join(self.data_dir, fname)
            logger.info(f"正在加载 {fname} ...")
            with open(fpath, 'r', encoding='utf-8') as f:
                for line in f:
                    self.raw_count += 1
                    try:
                        data = json.loads(line.strip())
                        # 简单校验关键字段
                        if all(k in data for k in ['user_id', 'action', 'ts']):
                            self.records.append(data)
                        else:
                            self.error_count += 1
                    except json.JSONDecodeError:
                        self.error_count += 1
        
        logger.info(f"✅ ODS 层加载完成：总行数 {self.raw_count}, 有效 {len(self.records)}, 丢弃 {self.error_count}")

    def transform_dwd(self):
        """DWD 层：数据清洗与标准化"""
        logger.info("🧹 开始 DWD 层清洗...")
        clean_data = []
        for rec in self.records:
            # 1. 数据标准化
            action = rec['action'].lower()
            amount = float(rec.get('amount', 0.0))
            
            # 2. 过滤异常值 (例如金额为负数)
            if amount < 0:
                continue
            
            # 3. 构建宽表记录
            clean_rec = {
                'date': rec['ts'].split(' ')[0],
                'hour': rec['ts'].split(' ')[1].split(':')[0],
                'user_id': rec['user_id'],
                'action': action,
                'category': rec.get('category', 'Unknown'),
                'amount': amount,
                'device': rec.get('device', 'Unknown')
            }
            clean_data.append(clean_rec)
        
        self.records = clean_data
        logger.info(f"✅ DWD 层清洗完成：剩余 {len(self.records)} 条明细数据")

    def aggregate_dws_ads(self):
        """DWS/ADS 层：聚合核心业务指标"""
        logger.info("📊 开始 DWS/ADS 层聚合计算...")
        
        # 初始化计数器
        uv_set = set()
        action_counts = defaultdict(int)
        category_gmv = defaultdict(float)
        device_counts = defaultdict(int)
        total_gmv = 0.0
        pay_users = set()
        view_users = set()

        for rec in self.records:
            uid = rec['user_id']
            action = rec['action']
            amt = rec['amount']
            cat = rec['category']
            dev = rec['device']

            # UV 统计
            uv_set.add(uid)
            
            # 行为统计
            action_counts[action] += 1
            
            # 设备统计
            device_counts[dev] += 1

            # GMV 统计 (仅支付行为)
            if action == 'pay':
                total_gmv += amt
                category_gmv[cat] += amt
                pay_users.add(uid)
            
            # 漏斗分析辅助
            if action == 'view':
                view_users.add(uid)

        # 计算转化率
        cart_users = set(r['user_id'] for r in self.records if r['action'] == 'cart')
        view_to_cart_rate = (len(cart_users) / len(view_users) * 100) if view_users else 0
        cart_to_pay_rate = (len(pay_users) / len(cart_users) * 100) if cart_users else 0

        # 整理结果
        top_categories = sorted(category_gmv.items(), key=lambda x: x[1], reverse=True)[:5]
        top_actions = sorted(action_counts.items(), key=lambda x: x[1], reverse=True)

        report = {
            "report_time": datetime.now().isoformat(),
            "metrics": {
                "total_records": len(self.records),
                "uv": len(uv_set),
                "total_gmv": round(total_gmv, 2),
                "avg_order_value": round(total_gmv / len(pay_users), 2) if pay_users else 0
            },
            "funnel": {
                "view_users": len(view_users),
                "cart_users": len(cart_users),
                "pay_users": len(pay_users),
                "view_to_cart_rate": f"{view_to_cart_rate:.2f}%",
                "cart_to_pay_rate": f"{cart_to_pay_rate:.2f}%"
            },
            "top_categories_gmv": dict(top_categories),
            "action_distribution": dict(top_actions),
            "device_distribution": dict(device_counts)
        }
        return report

    def save_results(self, report):
        """保存结果"""
        # 保存 JSON
        json_path = os.path.join(self.output_dir, "ads_business_report.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # 保存可读文本
        txt_path = os.path.join(self.output_dir, "ads_business_report.txt")
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(f"=== 数据仓库 Day 5 业务日报 ===\n")
            f.write(f"生成时间：{report['report_time']}\n\n")
            
            f.write(f"【核心指标】\n")
            m = report['metrics']
            f.write(f"  - 处理记录数：{m['total_records']:,}\n")
            f.write(f"  - 独立用户数 (UV)：{m['uv']:,}\n")
            f.write(f"  - 总成交额 (GMV)：¥ {m['total_gmv']:,.2f}\n")
            f.write(f"  - 客单价 (AOV)：¥ {m['avg_order_value']:,.2f}\n\n")
            
            f.write(f"【转化漏斗】\n")
            fun = report['funnel']
            f.write(f"  - 浏览用户：{fun['view_users']:,}\n")
            f.write(f"  - 加购用户：{fun['cart_users']:,} (转化率 {fun['view_to_cart_rate']})\n")
            f.write(f"  - 支付用户：{fun['pay_users']:,} (转化率 {fun['cart_to_pay_rate']})\n\n")
            
            f.write(f"【品类 GMV Top 5】\n")
            for cat, gmv in report['top_categories_gmv'].items():
                f.write(f"  - {cat}: ¥ {gmv:,.2f}\n")
            
            f.write(f"\n【行为分布】\n")
            for act, cnt in report['action_distribution'].items():
                f.write(f"  - {act}: {cnt:,}\n")

        logger.info(f"📄 报告已保存至：\n   - {json_path}\n   - {txt_path}")

    def run(self):
        start_time = datetime.now()
        logger.info("="*50)
        logger.info("🚀 启动生产级 ETL 流水线 (Day 5)")
        logger.info("="*50)
        
        try:
            self.extract_ods()
            self.transform_dwd()
            report = self.aggregate_dws_ads()
            self.save_results(report)
            
            duration = (datetime.now() - start_time).total_seconds()
            logger.info("="*50)
            logger.info(f"✅ 流水线执行成功！总耗时：{duration:.2f} 秒")
            logger.info(f"💡 关键成果：GMV ¥{report['metrics']['total_gmv']:,.2f}, UV {report['metrics']['uv']}")
            logger.info("="*50)
            return True
        except Exception as e:
            logger.error(f"❌ 流水线失败：{e}", exc_info=True)
            return False

if __name__ == "__main__":
    pipeline = BusinessETLPipeline()
    success = pipeline.run()
    sys.exit(0 if success else 1)
