import logging
from pyspark.sql import SparkSession

def create_spark_connection():
    s_conn = None
    spark_master_ip = 'localhost'  # Replace with the actual Spark Master container IP address

    try:
        s_conn = SparkSession.builder \
            .appName('SparkKafkaTest') \
            .master(f'spark://{spark_master_ip}:7077') \
            .config('spark.jars.packages',
                    "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,"
                    "org.apache.kafka:kafka-clients:3.3.2,"
                    "org.apache.spark:spark-token-provider-kafka-0-10_2.12:3.4.1,"
                    "org.apache.kafka:kafka_2.12:3.3.2") \
            .getOrCreate()
        s_conn.sparkContext.setLogLevel("ERROR")
        logging.info("Spark connection created successfully!")
    except Exception as e:
        logging.error(f"Couldn't create the spark session due to exception {e}")

    return s_conn

def connect_to_kafka(spark_conn):
    spark_df = None
    try:
        spark_df = spark_conn.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', 'localhost:9092') \
            .option('subscribe', 'users_created') \
            .option('startingOffsets', 'earliest') \
            .load()
        logging.info("Kafka DataFrame created successfully")
    except Exception as e:
        logging.warning(f"Kafka DataFrame could not be created because: {e}")

    return spark_df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    spark_conn = create_spark_connection()
    if spark_conn:
        kafka_df = connect_to_kafka(spark_conn)
        if kafka_df:
            logging.info("Kafka connection tested successfully!")
        else:
            logging.error("Failed to create Kafka DataFrame.")
    else:
        logging.error("Failed to create Spark session.")