-- ==================================================
-- Table: dwd_user_behavior_detail
-- Layer: DWD (Data Warehouse Detail)
-- Description: Parsed and cleaned user behavior data from ODS JSON logs
-- Created: 2026-02-26 (Day 2)
-- ==================================================

USE ecommerce_dw;

-- 1. Create Table (ORC format for high performance)
DROP TABLE IF EXISTS dwd_user_behavior_detail;
CREATE EXTERNAL TABLE dwd_user_behavior_detail (
    ts STRING,          -- Timestamp
    user_id STRING,     -- User ID
    product_id STRING,  -- Product ID
    product_name STRING,-- Product Name
    category STRING,    -- Category
    action STRING,      -- Action (view, cart, order, pay)
    amount DOUBLE,      -- Transaction Amount
    ip STRING,          -- IP Address
    device STRING       -- Device Type
)
PARTITIONED BY (dt STRING)
STORED AS ORC;

-- 2. Load Data (ETL from ODS)
-- Note: For limited resources (2vCPU/4GB), use Local Mode to avoid YARN OOM.
SET mapreduce.framework.name=local;
SET hive.exec.mode.local.auto=true;
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;

INSERT OVERWRITE TABLE dwd_user_behavior_detail PARTITION (dt)
SELECT 
    get_json_object(log_line, '$.ts') AS ts,
    get_json_object(log_line, '$.user_id') AS user_id,
    get_json_object(log_line, '$.product_id') AS product_id,
    get_json_object(log_line, '$.product_name') AS product_name,
    get_json_object(log_line, '$.category') AS category,
    get_json_object(log_line, '$.action') AS action,
    CAST(get_json_object(log_line, '$.amount') AS DOUBLE) AS amount,
    get_json_object(log_line, '$.ip') AS ip,
    get_json_object(log_line, '$.device') AS device,
    dt
FROM ods_user_behavior_log
WHERE dt = '2026-02-26';

-- 3. Verification Query
-- SELECT action, count(*) as cnt FROM dwd_user_behavior_detail WHERE dt='2026-02-26' GROUP BY action;
