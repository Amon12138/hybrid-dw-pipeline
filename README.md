# 🚀 Hybrid DW Pipeline

> **A lightweight, full-stack E-commerce Data Warehouse built on limited resources (2 vCPU/4GB RAM).**
> Features hybrid **offline** (Hive/Spark) and **real-time** (Kafka/Flink) pipelines.

## 📅 Project Start
**2026-02-25**

## 🎯 Goal
Build a complete data warehouse on a **2-core 4G ECS** in 8 days.
- **Offline**: ODS -> DWD -> DWS -> ADS (Hive/Spark)
- **Real-time**: Kafka + Flink
- **Focus**: Resource tuning, troubleshooting, and end-to-end architecture.

## 🛠️ Tech Stack
| Component | Version | Status | Notes |
|-----------|---------|--------|-------|
| **OS** | Ubuntu 22.04 | ✅ | 2 vCPU / 4GB RAM |
| **Hadoop** | 3.4.1 | ✅ | Optimized for Low Memory |
| **MySQL** | 8.0 | ✅ | Hive Metastore |
| **Hive** | 3.1.3 | ✅ | **Local Mode** Optimized |
| **Spark/Flink** | Latest | ⏳ | Coming Soon |
| **Kafka** | 3.5.2 | ⏳ | Coming Soon |

## 📝 Daily Progress (8-Day Sprint)
- [x] **Day 1 (02-25)**: Env Setup, Python Data Gen (100k), HDFS Upload, Hive ODS Layer
- [x] **Day 2 (02-26)**: DWD Layer (JSON->ORC), **Local Mode** (Solved YARN OOM), Funnel Analysis
- [ ] **Day 3 (02-27)**: DWS Layer - Aggregation (DAU, GMV, Retention)
- [ ] **Day 4 (02-28)**: ADS Layer - Business Metrics & Reporting
- [ ] **Day 5 (03-01)**: Spark SQL ETL - Performance Comparison
- [ ] **Day 6 (03-02)**: Kafka + Flink Real-time Pipeline
- [ ] **Day 7 (03-03)**: BI Visualization & Dashboard
- [ ] **Day 8 (03-04)**: Final Polish, Documentation & Interview Prep

## 💡 Key Challenges Solved
1. **YARN OOM**: Used **Local Mode** for small datasets to bypass container limits.
2. **MySQL Auth**: Fixed  for Hive 3.x compatibility.
3. **HDFS Safe Mode**: Resolved via Safe mode is OFF.
4. **Storage**: Converted Text (ODS) to **ORC** (DWD) for better performance.

## 👤 Author
**Amon12138** | Data Engineer Candidate
