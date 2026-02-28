-- ADS Layer: Daily Business Report
USE ecommerce_dw;

DROP TABLE IF EXISTS ads_daily_report;
CREATE EXTERNAL TABLE ads_daily_report (
    stat_date STRING, dau BIGINT, view_cnt BIGINT,
    cart_users BIGINT, order_users BIGINT, pay_users BIGINT,
    pay_rate DOUBLE, gmv DOUBLE, avg_order_value DOUBLE,
    top_category STRING, top_product_name STRING
)
PARTITIONED BY (dt STRING) STORED AS ORC;

INSERT OVERWRITE TABLE ads_daily_report PARTITION (dt='2026-02-26')
SELECT 
    '2026-02-26', count(*), sum(view_cnt),
    sum(case when cart_cnt > 0 then 1 else 0 end),
    sum(case when order_cnt > 0 then 1 else 0 end),
    sum(is_pay), round(sum(is_pay)*100.0/count(*), 2),
    sum(pay_amount), round(sum(pay_amount)/nullif(sum(pay_cnt),0), 2),
    (SELECT category FROM dws_product_day_stat WHERE dt='2026-02-26' ORDER BY gmv DESC LIMIT 1),
    (SELECT product_name FROM dws_product_day_stat WHERE dt='2026-02-26' ORDER BY gmv DESC LIMIT 1)
FROM dws_user_day_stat WHERE dt='2026-02-26';
