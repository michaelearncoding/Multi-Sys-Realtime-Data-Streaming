import logging
from pyspark.sql import SparkSession

def create_spark_connection():
    s_conn = None
    spark_master_ip = 'localhost'  # Replace with the actual Spark Master container IP address

    try:
        s_conn = SparkSession.builder \
            .appName('SparkDataStreaming') \
            .master(f'spark://{spark_master_ip}:7077') \
            .config('spark.jars.packages', "com.datastax.spark:spark-cassandra-connector_2.12:3.4.1,"
                                           "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,"
                                           "org.apache.kafka:kafka-clients:3.3.2") \
            .config('spark.cassandra.connection.host', '127.0.0.1') \
            .getOrCreate()
        s_conn.sparkContext.setLogLevel("ERROR")
        logging.info("Spark connection created successfully!")
    except Exception as e:
        logging.error(f"Couldn't create the spark session due to exception {e}")

    return s_conn

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    spark_conn = create_spark_connection()
    if spark_conn:
        logging.info("Spark session created successfully!")
    else:
        logging.error("Failed to create Spark session.")