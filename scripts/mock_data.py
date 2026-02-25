#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
from datetime import datetime, timedelta

# ================= 配置区域 =================
OUTPUT_FILE = "../data/user_behavior_2026-02-26.log"
TOTAL_RECORDS = 100000  # 生成 10 万条数据 (约 20MB，适合小内存)
BASE_DATE = "2026-02-26" # 数据日期

# 模拟数据池
USER_POOL = [f"user_{i:04d}" for i in range(1, 501)]  # 500 个用户
PRODUCT_POOL = [
    {"id": f"p_{i:03d}", "name": f"Product_{i}", "category": random.choice(["Electronics", "Clothing", "Home", "Books"]), "price": round(random.uniform(10.0, 500.0), 2)}
    for i in range(1, 101)  # 100 种商品
]

# 行为类型及权重 (浏览最多，支付最少)
ACTIONS = [
    ("view", 50),   # 浏览
    ("cart", 30),   # 加购
    ("order", 15),  # 下单
    ("pay", 5)      # 支付
]

# ================= 核心逻辑 =================
def generate_log():
    print(f"🚀 Start generating {TOTAL_RECORDS} records...")
    
    base_time = datetime.strptime(BASE_DATE, "%Y-%m-%d")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i in range(TOTAL_RECORDS):
            # 1. 随机时间 (当天 00:00:00 到 23:59:59)
            random_seconds = random.randint(0, 86399)
            ts = base_time + timedelta(seconds=random_seconds)
            
            # 2. 随机用户
            user_id = random.choice(USER_POOL)
            
            # 3. 随机商品
            product = random.choice(PRODUCT_POOL)
            
            # 4. 随机行为 (带权重)
            action = random.choices([a[0] for a in ACTIONS], weights=[a[1] for a in ACTIONS])[0]
            
            # 5. 金额 (只有 order 和 pay 有金额)
            amount = product["price"] if action in ["order", "pay"] else 0.0
            
            # 6. 构造日志对象 (JSON)
            log_entry = {
                "ts": ts.strftime("%Y-%m-%d %H:%M:%S"),
                "user_id": user_id,
                "product_id": product["id"],
                "product_name": product["name"],
                "category": product["category"],
                "action": action,
                "amount": amount,
                "ip": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                "device": random.choice(["iOS", "Android", "Web"])
            }
            
            # 7. 写入文件 (一行一个 JSON)
            f.write(json.dumps(log_entry) + "\n")
            
            # 进度提示
            if (i + 1) % 20000 == 0:
                print(f"   ... Generated {i+1} records")

    print(f"✅ Done! File saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_log()


