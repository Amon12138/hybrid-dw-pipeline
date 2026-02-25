-- ==================================================
-- Table: ods_user_behavior_log
-- Layer: ODS (Operational Data Store)
-- Description: Raw user behavior logs (JSON format)
-- Created: 2026-02-27
-- ==================================================

USE ecommerce_dw;

DROP TABLE IF EXISTS ods_user_behavior_log;
CREATE EXTERNAL TABLE ods_user_behavior_log (
    log_line STRING
)
PARTITIONED BY (dt STRING)
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/ecommerce_dw.db/ods_user_behavior_log';

-- Add partition manually (Alternative to MSCK REPAIR for specific dates)
ALTER TABLE ods_user_behavior_log ADD PARTITION (dt='2026-02-26') 
LOCATION '/user/hive/warehouse/ecommerce_dw.db/ods_user_behavior_log/dt=2026-02-26';

-- Verification Query
-- SELECT count(*) FROM ods_user_behavior_log WHERE dt='2026-02-26';
