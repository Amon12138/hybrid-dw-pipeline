# 🚀 Hybrid DW Pipeline

> **Description**: A lightweight, full-stack E-commerce Data Warehouse built on limited resources (2 vCPU/4GB RAM). Features hybrid offline (Hive/Spark) and real-time (Kafka/Flink) pipelines with optimized memory tuning.

## 📅 Start Date
2026-02-25

## 🎯 Project Goal
Build a complete **Offline + Real-time** data warehouse on a **2-core 4G Alibaba Cloud ECS**, demonstrating deep understanding of resource tuning and architecture design.

## 🛠️ Tech Stack & Versions
| Component | Version | Status |
|-----------|---------|--------|
| **Hadoop**    | 3.4.1   | ✅ Running (1 NN, 2 DN, 1 RM, 2 NM) |
| **Hive**      | 3.1.3   | ✅ Ready |
| **Spark**     | 3.4.1   | ✅ Ready |
| **Flink**     | 1.18.1  | ✅ Ready |
| **Kafka**     | 3.5.2   | ✅ Ready |
| **Java**      | 11      | ✅ Ready |

## 📝 Daily Progress
- [x] **Day 1 (2026-02-25)**: 
  - Ubuntu 22.04 Environment Configured
  - All Big Data Components Verified & Running
  - Git Repository Initialized
- [ ] Day 2: Python Data Generator...

## 💡 Key Challenges
- **Resource Constraints**: Optimizing for 2 vCPU / 4GB RAM.
- **OOM Prevention**: Tuning JVM heaps, YARN containers, and Spark/Flink memory.
- **Architecture**: Balancing offline batch processing and real-time streaming.

## 👤 Author
Amon12138
