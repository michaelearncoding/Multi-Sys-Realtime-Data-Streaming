# Realtime-Data-Streaming
Real time data engineering project.

Author: Qingda(Michael) Mai

This data engineering project that uses Docker, Apache Airflow, Apache Kafka, Apache Spark, Apache Cassandra, and PostgreSQL.

Architecture Overview

Data Ingestion: Raw data is ingested into the system using Kafka. The data can come from various sources like IoT devices, user activity logs, etc.

Data Processing: Airflow schedules Spark jobs to process the raw data. The processed data can either be aggregated, filtered, or transformed based on the business logic.

Data Storage: The processed data is stored in either Cassandra for NoSQL needs or PostgreSQL for relational data storage.

Deployment: Docker containers encapsulate each component of the architecture, ensuring isolation and ease of deployment.


Summary:  This project is building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra.

![](https://github.com/michaelearncoding/Realtime-Data-Streaming/blob/main/Data%20engineering%20architecture.png?raw=true)
