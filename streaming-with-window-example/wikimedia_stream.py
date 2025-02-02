import os
import pyspark
import time
from kafka import KafkaProducer
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.streaming import StreamingContext
from sseclient import SSEClient

os.environ['SPARK_HOME'] = "/Users/ran/pyspark/.venv/lib/python3.11/site-packages/pyspark/"
os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'
os.environ['PYSPARK_PYTHON'] = 'python'

# Note! Update PYSPARK_SUBMIT_ARGS value with your pyspark version. in the line below it is "3.5.4"
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'
URL = 'https://stream.wikimedia.org/v2/stream/recentchange'

KAFKA_BROKER_URL = "localhost:9092"
KAFKA_TOPIC = "wikimedia_topic_window_1"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
)

def stream_to_kafka():

     events = SSEClient(URL)
     while True:
         time.sleep(0.5)
         for event in events:
             if event.event == 'message' and event.data != None:
                 message = event.data.encode("utf-8")
                 producer.send(KAFKA_TOPIC, value=message)
                 break

if __name__ == "__main__":
    # print(f"Streaming events from {URL} to Kafka topic '{KAFKA_TOPIC}'")
    stream_to_kafka()
