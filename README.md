# Realtime-Data-Streaming
Real time data engineering project.

Author: Qingda(Michael) Mai


**Summary**:  This project is building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra.

Architecture Overview

1) Data Ingestion: Raw data is ingested into the system using  `Kafka`. The data can come from various sources like IoT devices, user activity logs, etc. In this project, we use Python API to parse the `JSON-type` data, more specifically, randomly generated customer information.

2) Data Processing: Airflow schedules Spark jobs to process the raw data. The processed data can either be aggregated, filtered, or transformed based on the business logic. In this project, we use Python programming language to write Airflow to schedule the jobs' flow. And use SQL & Python to transform the `NOSQL` recognizable object into the `pyspark` recognizable object.

3) Data Storage: The processed data is stored in either Cassandra for NoSQL needs or PostgreSQL for relational data storage.

4) Deployment: Docker containers encapsulate each component of the architecture, ensuring isolation and ease of deployment.

![](https://github.com/michaelearncoding/Realtime-Data-Streaming/blob/main/Data%20engineering%20architecture.png?raw=true)

Reference:
[1] https://python.plainenglish.io/realtime-data-engineering-project-with-airflow-kafka-spark-cassandra-and-postgres-804bcd963974
[2] https://www.youtube.com/watch?v=GqAcTrqKcrY
[3] Related technique offical document : 
✅ Docker Compose Documentation: https://docs.docker.com/compose/
✅ Apache Kafka Official Site: https://kafka.apache.org/
✅ Apache Spark Official Site: https://spark.apache.org/
✅ Apache Airflow Official Site: https://airflow.apache.org/
✅ Cassandra: https://cassandra.apache.org/
✅ Confluent Docs: https://docs.confluent.io/home/overvi...

