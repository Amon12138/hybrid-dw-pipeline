#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/day6_spark_etl.py"

# 确保环境变量已设置 (如果外部没设，这里再次确认)
if [ -z "$HADOOP_CONF_DIR" ]; then
    export HADOOP_CONF_DIR=$(find /etc /opt -name "yarn-site.xml" 2>/dev/null | head -n 1 | xargs dirname)
fi

echo "🔥 Starting Spark Job..."
echo "📂 Script: $PY_SCRIPT"
echo "⚙️  Config: $HADOOP_CONF_DIR"

spark-submit \
  --master yarn \
  --deploy-mode client \
  --name "Day6-Spark-ETL-Lightweight" \
  --conf spark.driver.memory=512m \
  --conf spark.executor.memory=512m \
  --conf spark.executor.cores=1 \
  --conf spark.driver.cores=1 \
  --conf spark.sql.shuffle.partitions=2 \
  --conf spark.default.parallelism=2 \
  --conf spark.yarn.executor.memoryOverhead=256 \
  --conf spark.yarn.driver.memoryOverhead=256 \
  --conf spark.sql.adaptive.enabled=true \
  --conf spark.yarn.conf.dir="$HADOOP_CONF_DIR" \
  "$PY_SCRIPT"

echo "✅ Job Finished"
