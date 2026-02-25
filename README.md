# 🚀 Hybrid DW Pipeline

> **A lightweight, full-stack E-commerce Data Warehouse built on limited resources (2 vCPU/4GB RAM).**
> Features hybrid **offline** (Hive/Spark) and **real-time** (Kafka/Flink) pipelines.

## 🛠️ Tech Stack
| Component | Version | Status | Notes |
|-----------|---------|--------|-------|
| **OS** | Ubuntu 22.04 | ✅ | 2 vCPU / 4GB RAM |
| **Hadoop** | 3.4.1 | ✅ Running | 1 NN, 2 DN, 1 RM, 2 NM |
| **MySQL** | 8.0 | ✅ Running | Hive Metastore |
| **Hive** | 3.1.3 | ✅ Ready | Configured with MySQL |
| **Spark** | 3.4.1 | ✅ Ready | Tuned for Low Memory |
| **Flink** | 1.18.1 | ✅ Ready | Standalone Mode |
| **Kafka** | 3.5.2 | ✅ Ready | Single Broker |

## 📝 Daily Progress
- [x] **Day 1**: Env Setup, Python Data Gen (100k), HDFS Upload, Hive ODS Layer
- [ ] **Day 2**: DWD Layer - JSON Parsing & Data Cleaning
- [ ] **Day 3**: DWS Layer - User/Product Aggregation
- [ ] **Day 4**: ADS Layer - Business Metrics (GMV, DAU)
- [ ] **Day 5**: Spark SQL ETL & Performance Tuning
- [ ] **Day 6**: Kafka Real-time Ingestion
- [ ] **Day 7**: Flink SQL Real-time Windowing
- [ ] **Day 8**: BI Visualization & Dashboard

## 💡 Key Challenges Solved
- **MySQL Metastore**: Fixed auth plugin ().
- **HDFS Path**: Manually aligned Hive LOCATION with HDFS paths.
- **Resource Limits**: Optimized for 2-core 4GB constraints.

## 👤 Author
**Amon12138** | Data Engineer Candidate
