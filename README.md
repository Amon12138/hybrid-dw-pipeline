# 🚀 Hybrid DW Pipeline

> **A lightweight, full-stack E-commerce Data Warehouse built on limited resources (2 vCPU/4GB RAM).**  
> Features hybrid **offline** (Hive/Spark/Python) and **real-time** (Kafka/Flink) pipelines.

## 📅 Project Start
**2026-02-25**

## 🎯 Goal
Build a complete data warehouse on a **2-core 4G ECS** in 8 days.
- **Offline**: ODS -> DWD -> DWS -> ADS (Hive & Python ETL)
- **Real-time**: Kafka + Flink
- **Focus**: Resource tuning, Troubleshooting & Production-Ready Scripts

## 🛠️ Tech Stack
| Component | Version | Status | Notes |
|-----------|---------|--------|-------|
| **OS** | Ubuntu 22.04 | ✅ | 2 vCPU / 4GB RAM |
| **Hadoop** | 3.4.1 | ✅ | Optimized Config |
| **MySQL** | 8.0 | ✅ | Hive Metastore |
| **Hive** | 3.1.3 | ✅ | Local Mode Optimized |
| **Python** | 3.8+ | ✅ | Production ETL Script (Day 5) |
| **Spark** | 3.4.1 | ⏳ | Pending for Large Scale |

## 📝 Daily Progress
- [x] **Day 1**: Env Setup, Data Gen (100k), ODS Layer
- [x] **Day 2**: DWD Layer (JSON->ORC), Solved YARN OOM
- [x] **Day 3**: DWS Layer (DAU, GMV, Retention)
- [x] **Day 4**: ADS Layer (Daily Report, MapJoin Opt)
- [x] **Day 5**: **Production ETL Pipeline** (Python JSON Parser, GMV/UV Calculation)
- [ ] **Day 6**: Kafka + Flink Real-time
- [ ] **Day 7**: BI Dashboard
- [ ] **Day 8**: Final Polish

## 💡 Key Challenges & Solutions

| Challenge | Solution | Impact |
| :--- | :--- | :--- |
| **YARN OOM** | Switched to **Local Mode** for small datasets | No more crashes, fast execution |
| **MySQL Auth** | Changed to `mysql_native_password` | Hive connected to MySQL 8.0 |
| **HDFS Safe Mode** | Used `hdfs dfsadmin -safemode leave` | Unblocked writes |
| **RunJar Hang** | Used `kill -9` and verified with `ps` | Freed 1GB memory |
| **XML Syntax** | Replaced file using `cat` to fix malformed tags | YARN started successfully |
| **ANY_VALUE Error** | Replaced with `MAX()` for compatibility | DWS aggregation succeeded |
| **Slow Subqueries** | Leveraged **MapJoin** for small result sets | Avoided Shuffle, faster ADS build |
| **Complex JSON Parsing** | Built custom Python parser with error handling | 100% data cleaning rate, robust ETL |
| **Memory Efficiency** | Stream processing (line-by-line) instead of loading all | Processed 100k logs in <4s on 4GB RAM |
| **Metric Accuracy** | Implemented strict deduplication for UV/GMV | Accurate business reporting |

## 📂 Project Structure
hybrid-dw-pipeline/
├── scripts/          
│   ├── gen_data.py             # Mock data generator
│   └── day5_full_pipeline_test.py  # Prod-ready ETL Script
├── sql/
│   ├── ods/            # Raw Logs
│   ├── dwd/            # Parsed ORC
│   ├── dws/            # Aggregated Metrics
│   └── ads/            # Business Reports
├── data/               # Mock Data (JSON Lines)
├── output/             # Generated Reports (JSON/TXT)
│   ├── ads_business_report.json
│   └── ads_business_report.txt
└── README.md

## 📊 Day 5 Highlights
- **Script**: `scripts/day5_full_pipeline_test.py`
- **Performance**: 100,000 records processed in **< 4 seconds**.
- **Metrics Calculated**: 
  - **GMV**: ¥1,348,876.15
  - **UV**: 500 Unique Users
  - **Conversion Funnel**: View -> Cart -> Pay
  - **Top Categories**: Electronics, Home, Books
- **Output**: Automated generation of `ads_business_report.json` and `.txt`.

## 👤 Author
**Amon12138** | Data Engineer Candidate
