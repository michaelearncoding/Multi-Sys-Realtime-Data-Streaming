import logging
import socket

from cassandra.cluster import Cluster, DCAwareRoundRobinPolicy
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

def create_keyspace(session):
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS spark_streams
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)
    logging.info("Keyspace created successfully!")

def create_table(session):
    session.execute("""
    CREATE TABLE IF NOT EXISTS spark_streams.created_users (
        id UUID PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        address TEXT,
        post_code TEXT,
        email TEXT,
        username TEXT,
        registered_date TEXT,
        phone TEXT,
        picture TEXT);
    """)
    logging.info("Table created successfully!")

def insert_data(session, **kwargs):
    logging.info("Inserting data...")
    try:
        session.execute("""
            INSERT INTO spark_streams.created_users(id, first_name, last_name, gender, address,
                post_code, email, username, dob, registered_date, phone, picture)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (kwargs.get('id'), kwargs.get('first_name'), kwargs.get('last_name'), kwargs.get('gender'),
              kwargs.get('address'), kwargs.get('post_code'), kwargs.get('email'), kwargs.get('username'),
              kwargs.get('dob'), kwargs.get('registered_date'), kwargs.get('phone'), kwargs.get('picture')))
        logging.info(f"Data inserted for {kwargs.get('first_name')} {kwargs.get('last_name')}")
    except Exception as e:
        logging.error(f"Could not insert data due to {e}")

def create_spark_connection():
    try:
        spark_conn = SparkSession.builder \
            .appName('SparkDataStreaming') \
            .master('spark://localhost:7077') \
            .master('local[*]') \
            .config('spark.jars.packages',
                    "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,"
                    "org.apache.kafka:kafka-clients:3.3.2,"
                    "org.apache.spark:spark-token-provider-kafka-0-10_2.12:3.4.1,"
                    "org.apache.commons:commons-pool2:2.12.0,"
                    # "com.datastax.spark:spark-cassandra-connector_2.12:3.5.1") 
                    "com.datastax.spark:spark-cassandra-connector-assembly_2.12:3.5.1")\
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

def connect_to_kafka(spark_conn):
    try:
        spark_df = spark_conn.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', 'localhost:9092') \
            .option('subscribe', 'users_created') \
            .option('startingOffsets', 'earliest') \
            .load()
        logging.info("Kafka DataFrame created successfully")
        return spark_df
    except Exception as e:
        logging.warning(f"Kafka DataFrame could not be created because: {e}")
        return None

def create_cassandra_connection():
    try:
        cluster = Cluster(
            contact_points=['127.0.0.1'],
            port=9042,
            load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'),
            protocol_version=5
        )

        cas_session = cluster.connect()

        logging.info("Cassandra connection created successfully!")

        # df = spark_conn.read \
        #     .format("org.apache.spark.sql.cassandra") \
        #     .options(table="created_users", keyspace="spark_streams") \
        #     .load()
        # df.show()

        return cas_session
    except Exception as e:
        logging.error(f"Could not create Cassandra connection due to {e}")
        return None

def create_selection_df_from_kafka(spark_df):
    if spark_df is None:
        logging.error("Kafka DataFrame is None. Cannot proceed with selection.")
        return None

    schema = StructType([
        StructField("id", StringType(), False),
        StructField("first_name", StringType(), False),
        StructField("last_name", StringType(), False),
        StructField("gender", StringType(), False),
        StructField("address", StringType(), False),
        StructField("post_code", StringType(), False),
        StructField("email", StringType(), False),
        StructField("username", StringType(), False),
        StructField("registered_date", StringType(), False),
        StructField("phone", StringType(), False),
        StructField("picture", StringType(), False)
    ])

    sel = spark_df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col('value'), schema).alias('data')).select("data.*")
    logging.info("Selection DataFrame created successfully")
    return sel

def write_to_cassandra(batch_df, batch_id):
    batch_df.write \
        .format("org.apache.spark.sql.cassandra") \
        .option('keyspace', 'spark_streams') \
        .option('table', 'created_users') \
        .mode('append') \
        .save()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Create Spark connection
    spark_conn = create_spark_connection()
    if spark_conn is None:
        logging.error("Failed to create Spark session.")
        exit(1)

    # Connect to Kafka
    spark_df = connect_to_kafka(spark_conn)
    if spark_df is None:
        logging.error("Failed to create Kafka DataFrame.")
        exit(1)

    # Create selection DataFrame from Kafka
    selection_df = create_selection_df_from_kafka(spark_df)
    if selection_df is None:
        logging.error("Failed to create selection DataFrame from Kafka.")
        exit(1)

    # Create Cassandra connection
    cas_session = create_cassandra_connection()
    if cas_session is None:
        logging.error("Failed to create Cassandra connection.")
        exit(1)

    # Create keyspace and table in Cassandra
    create_keyspace(cas_session)
    create_table(cas_session)

    # Start streaming query
    # The below part is not fixed yet, the streaming query is not working as expected
    # try:
    #     streaming_query = (selection_df.writeStream
    #                        .format("org.apache.spark.sql.cassandra")
    #                        .option('checkpointLocation', '/tmp/checkpoint')
    #                        .option('keyspace', 'spark_streams')
    #                        .option('table', 'created_users')
    #                        .start())
    #     streaming_query.awaitTermination()
    # except Exception as e:
    #     logging.error(f"Streaming query failed due to {e}")
    #     exit(1)

    # Same as above, the streaming query is not working as expected
    # here use foreachBatch to write to Cassandra
    try:
        streaming_query = selection_df.writeStream \
            .foreachBatch(write_to_cassandra) \
            .option('checkpointLocation', '/tmp/checkpoint') \
            .start()
        streaming_query.awaitTermination()
    except Exception as e:
        logging.error(f"Streaming query failed due to {e}")
        exit(1)