from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, count
from pyspark.sql.types import StructType, StringType, LongType

# Define the schema for events
schema = StructType() \
    .add("timestamp", StringType()) \
    .add("visitorid", StringType()) \
    .add("event", StringType()) \
    .add("itemid", StringType()) \
    .add("transactionid", StringType())

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Read Kafka stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "retail_events") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse Kafka message value as JSON
events_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Count events in real-time
event_counts = events_df.groupBy("event").count()

# Write stream to console
query = event_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
