# Realtime-Data-Streaming
Real time data engineering project.

Author: Qingda(Michael) Mai

😄Introduction (Tech I use in this project)

- Setting up a data pipeline with Apache Airflow
- Real-time data streaming with Apache Kafka
- Distributed synchronization with Apache Zookeeper
- Data processing techniques with Apache Spark
- Data storage solutions with Cassandra and PostgreSQL
- Containerizing your entire data engineering setup with Docker
  
**Summary**:  This project is building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra.

---
⚡Toolbox

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" alt="Python Logo" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/pytorch/pytorch-original-wordmark.svg" alt="Pytorch Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg" alt="SQL Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/linux/linux-original.svg" alt="Linux Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/matlab/matlab-original.svg" alt="MATLAB Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/r/r-original.svg" alt="R Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original-wordmark.svg" alt="Jupyter Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/jenkins/jenkins-original.svg" alt="Jenkins Logo" width="50" height="50"><img src="https://github.com/devicons/devicon/blob/master/icons/java/java-original-wordmark.svg" alt="Java Logo" width="50" height="50">
<img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" alt="Git Logo" width="50" height="50" />
<img src="https://github.com/devicons/devicon/blob/master/icons/azure/azure-original-wordmark.svg" alt="Azure Logo" width="50" height="50" />
<img src="https://github.com/devicons/devicon/blob/master/icons/microsoftsqlserver/microsoftsqlserver-plain-wordmark.svg" alt="SQLSERVER Logo" width="50" height="50" />

`Technologies`

Apache Airflow

Python

Apache Kafka

Apache Zookeeper

Apache Spark

Cassandra

PostgreSQL

Docker

![image](https://github.com/michaelearncoding/Realtime-Data-Streaming/assets/47378073/1cca2d76-404c-4c58-83e6-484742df9235)


![](https://github.com/michaelearncoding/Realtime-Data-Streaming/blob/main/Data%20engineering%20architecture.png?raw=true)

Architecture Overview

1) Data Ingestion: Raw data is ingested into the system using  `Kafka`. The data can come from various sources like IoT devices, user activity logs, etc. In this project, we use Python API to parse the `JSON-type` data, more specifically, randomly generated customer information.

2) Data Processing: Airflow schedules Spark jobs to process the raw data. The processed data can either be aggregated, filtered, or transformed based on the business logic. In this project, we use Python programming language to write Airflow to schedule the jobs' flow. And use SQL & Python to transform the `NOSQL` recognizable object into the `pyspark` recognizable object.

3) Data Storage: The processed data is stored in either Cassandra for NoSQL needs or PostgreSQL for relational data storage.

4) Deployment: Docker containers encapsulate each component of the architecture, ensuring isolation and ease of deployment.

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

