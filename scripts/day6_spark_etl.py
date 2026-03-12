from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum as _sum, avg, lit
from pyspark.sql.types import DoubleType
import os
import shutil

# =================配置区域=================
INPUT_PATH = "file:///root/my-data-warehouse/data/user_behavior_2026-02-26.log"
OUTPUT_PATH = "file:///root/my-data-warehouse/data/output/day6_result"
# =========================================

def main():
    print("⚡ 正在创建 Spark Session...")
    spark = SparkSession.builder \
        .appName("Day6-Spark-ETL-Fixed") \
        .master("yarn") \
        .config("spark.executor.memory", "512m") \
        .config("spark.driver.memory", "512m") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")
    print("✅ Spark Session 创建成功!")

    try:
        # 1. 读取数据
        print(f"📖 正在读取数据: {INPUT_PATH} ...")
        df_raw = spark.read.json(INPUT_PATH)
        row_count = df_raw.count()
        print(f"✅ 成功加载 {row_count} 条记录.")

        # 2. 数据清洗 (使用正确的列名: action, amount)
        print("🧹 正在清洗数据...")
        df_clean = df_raw.filter(
            col("action").isNotNull() & 
            (col("amount").cast(DoubleType()) >= 0)
        )
        clean_count = df_clean.count()
        print(f"🧹 清洗后剩余 {clean_count} 条有效记录.")

        # 3. 数据转换
        print("🔄 正在转换数据...")
        df_transformed = df_clean.withColumn("dt", lit("2026-02-26"))

        # 4. 聚合统计
        print("📊 正在计算统计指标...")
        df_stats = df_transformed.groupBy("action", "category", "dt").agg(
            count("*").alias("event_count"),
            _sum("amount").alias("total_amount"),
            avg("amount").alias("avg_amount")
        ).orderBy("event_count", ascending=False)

        print("📈 统计结果预览:")
        df_stats.show(10, truncate=False)

        # 5. 写入结果
        print(f"💾 正在保存结果到: {OUTPUT_PATH} ...")
        local_out_path = OUTPUT_PATH.replace("file://", "")
        
        # 如果目录存在则删除 (Spark overwrite 模式有时对本地文件系统支持不好，手动删更稳)
        if os.path.exists(local_out_path):
            shutil.rmtree(local_out_path)
            print(f"⚠️  已清理旧目录: {local_out_path}")

        df_stats.write.mode("overwrite").parquet(OUTPUT_PATH)
        print(f"✅ 任务完成！结果已保存至: {OUTPUT_PATH}")

    except Exception as e:
        print(f"❌ 任务执行失败: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("🛑 正在停止 Spark Session...")
        spark.stop()
        print("👋 再见!")

if __name__ == "__main__":
    main()
