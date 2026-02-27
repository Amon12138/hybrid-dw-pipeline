-- ==================================================
-- Layer: DWS (Data Warehouse Service)
-- Description: Daily Aggregation for Users and Products
-- Created: 2026-02-27 (Day 3)
-- ==================================================

USE ecommerce_dw;

-- 1. User Daily Stats
DROP TABLE IF EXISTS dws_user_day_stat;
CREATE EXTERNAL TABLE dws_user_day_stat (
    user_id STRING,
    view_cnt INT,
    cart_cnt INT,
    order_cnt INT,
    pay_cnt INT,
    pay_amount DOUBLE,
    is_pay BIGINT
)
PARTITIONED BY (dt STRING)
STORED AS ORC;

INSERT OVERWRITE TABLE dws_user_day_stat PARTITION (dt)
SELECT 
    user_id,
    SUM(CASE WHEN action = 'view' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'cart' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'order' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'pay' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'pay' THEN amount ELSE 0 END),
    MAX(CASE WHEN action = 'pay' THEN 1 ELSE 0 END),
    dt
FROM dwd_user_behavior_detail
WHERE dt = '2026-02-26'
GROUP BY user_id, dt;

-- 2. Product Daily Stats
DROP TABLE IF EXISTS dws_product_day_stat;
CREATE EXTERNAL TABLE dws_product_day_stat (
    product_id STRING,
    product_name STRING,
    category STRING,
    view_cnt INT,
    cart_cnt INT,
    order_cnt INT,
    pay_cnt INT,
    gmv DOUBLE,
    pay_users BIGINT
)
PARTITIONED BY (dt STRING)
STORED AS ORC;

-- Note: Used MAX() instead of ANY_VALUE() for compatibility
INSERT OVERWRITE TABLE dws_product_day_stat PARTITION (dt)
SELECT 
    product_id,
    MAX(product_name),
    MAX(category),
    SUM(CASE WHEN action = 'view' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'cart' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'order' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'pay' THEN 1 ELSE 0 END),
    SUM(CASE WHEN action = 'pay' THEN amount ELSE 0 END),
    COUNT(DISTINCT CASE WHEN action = 'pay' THEN user_id END),
    dt
FROM dwd_user_behavior_detail
WHERE dt = '2026-02-26'
GROUP BY product_id, dt;
