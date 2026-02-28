# 🚀 Hybrid DW Pipeline

> **A lightweight, full-stack E-commerce Data Warehouse built on limited resources (2 vCPU/4GB RAM).**  
> Features hybrid **offline** (Hive/Spark) and **real-time** (Kafka/Flink) pipelines.

## 📅 Project Start
**2026-02-25**

## 🎯 Goal
Build a complete data warehouse on a **2-core 4G ECS** in 8 days.
- **Offline**: ODS -> DWD -> DWS -> ADS
- **Real-time**: Kafka + Flink
- **Focus**: Resource tuning & Troubleshooting

## 🛠️ Tech Stack
| Component | Version | Status | Notes |
|-----------|---------|--------|-------|
| **OS** | Ubuntu 22.04 | ✅ | 2 vCPU / 4GB RAM |
| **Hadoop** | 3.4.1 | ✅ | Optimized Config |
| **MySQL** | 8.0 | ✅ | Hive Metastore |
| **Hive** | 3.1.3 | ✅ | Local Mode Optimized |
| **Spark** | 3.4.1 | ⏳ | Day 5 |

## 📝 Daily Progress
- [x] **Day 1**: Env Setup, Data Gen (100k), ODS Layer
- [x] **Day 2**: DWD Layer (JSON->ORC), Solved YARN OOM
- [x] **Day 3**: DWS Layer (DAU, GMV, Retention)
- [x] **Day 4**: ADS Layer (Daily Report, MapJoin Opt)
- [ ] **Day 5**: Spark SQL Performance Test
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

## 📂 Project Structure
```text
hybrid-dw-pipeline/
├── scripts/          # Python generators
├── sql/
│   ├── ods/          # Raw Logs
│   ├── dwd/          # Parsed ORC
│   ├── dws/          # Aggregated Metrics
│   └── ads/          # Business Reports
├── data/             # Mock Data
└── README.md
```

## 👤 Author
**Amon12138** | Data Engineer Candidate
