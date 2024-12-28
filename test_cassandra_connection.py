# import logging
# from cassandra.cluster import Cluster, DCAwareRoundRobinPolicy
#
# def create_cassandra_connection():
#     try:
#         cluster = Cluster(
#             contact_points=['cassandra_db'],  # 使用主机的IP地址
#             port=9042,  # 指定Cassandra的端口
#             load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'),
#             protocol_version=5  # Specify the protocol version
#         )
#
#         cas_session = cluster.connect()
#         logging.info("Cassandra connection created successfully!")
#         return cas_session
#     except Exception as e:
#         logging.error(f"Could not create cassandra connection due to {e}")
#         return None
# if __name__ == "__main__":
#     session = create_cassandra_connection()
#     if session:
#         print("Connected to Cassandra")
#     else:
#         print("Failed to connect to Cassandra")

import logging
from pyspark.sql import SparkSession

def create_spark_connection():
    try:
        spark_conn = SparkSession.builder \
            .appName('SparkCassandraTest') \
            .master('local[*]') \
            .config('spark.jars', '/path/to/spark-cassandra-connector-assembly_2.12-3.2.0.jar') \
            .config('spark.cassandra.connection.host', 'localhost') \
            .config('spark.cassandra.connection.port', '9042') \
            .config('spark.cassandra.auth.username', 'cassandra') \
            .config('spark.cassandra.auth.password', 'cassandra') \
            .getOrCreate()
        spark_conn.sparkContext.setLogLevel("ERROR")
        logging.info("Spark connection created successfully!")
        return spark_conn
    except Exception as e:
        logging.error(f"Couldn't create the spark session due to exception {e}")
        return None

def test_spark_cassandra_connection():
    spark_conn = create_spark_connection()
    if spark_conn is None:
        logging.error("Failed to create Spark session.")
        return

    try:
        df = spark_conn.read \
            .format("org.apache.spark.sql.cassandra") \
            .options(table="created_users", keyspace="spark_streams") \
            .load()
        df.show()
        logging.info("Successfully connected to Cassandra and read data.")
    except Exception as e:
        logging.error(f"Failed to read from Cassandra due to {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_spark_cassandra_connection()