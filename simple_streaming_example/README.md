# Pyspark Streaming Jupyter Tutorial
Tutorial for Pyspark Structured Streaming with Kafka + Jupyter

## Prerequisites
1. Install Java JRE 1.8
Java JRE 1.8 is required to work well with PySpark. Newer versions may not work

Make sure JAVA_HOME is set:
```bash
echo $JAVA_HOME
```

## Setup
1. Check your Python Version. Obtain 3.9 version (or any version that is compatible with PySpark3.2 Structure Streaming)
```bash
python3.9 --version
```
2. Open Python venv
```bash
python3.9 -m venv .venv3.9
source .venv3.9/bin/activate
```
3. Install necessary packages
```bash
pip install jupyter
pip install kafka-python
pip install pyspark==3.2.0
pip install findspark
pip install requests
pip install sseclient
```
4. Run Jupyter
For local machine, run:
```bash
jupyter-notebook 
```
A browser will be opened.

If you run on local PC, skip to step 5.

In case you run linux on EC2 virtual machine and not on your local PC, run:
```bash
jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser
```
then open the broser with the url http://<your_buclic_ec2_ip>:8888
The UI will prompt for a token. Obtain the token from the console output

5. Open a notebook
- In the web console that opens, open a new notebook of Python 3
6. Test a demo notebook (Note that you need Kafka broker running. See below)
- Copy the content of the file [pyspark_structured_streaming.ipynb](https://github.com/ransilberman/pyspark-streaming-jupyter-tutorial/blob/main/simple_streaming_example/pyspark_structured_streaming.ipynb)
- Replace the `SPARK_HOME` value with the SPARK_HOME that you obtained in step #4.
- Replace the PYSPARK_VERSION with the version you obtained above

## Kafka Debug
1. Start Kafka in container
```bash
docker run -p 9092:9092 apache/kafka:latest
```
In order to view Kafka topics and debug, follow those steps:
2. Obtain the docker CONTAINER ID:
```bash
docker ps
```
You will see the result:
```bash
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                    NAMES
abc123def456   apache/kafka:latest   "some-command-here"     10 minutes ago  Up 10 minutes  0.0.0.0:9092->9092/tcp   kafka_container
```
3. Run the following command to list Kafka topics:
```bash
docker exec -it <container_id_or_name> /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```
Result may look like the following:
```bash
wikimedia_topic_1
```
4. Describe a certain topic:
```bash
docker exec -it <container_id_or_name> /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic <topic_name>
```
Result may look like this:
```bash
Topic: wikimedia_topic_1	TopicId: 1PFZVJkIT9ex7Cx-AycgtA	PartitionCount: 1	ReplicationFactor: 1	Configs: segment.bytes=1073741824
	Topic: wikimedia_topic_1	Partition: 0	Leader: 1	Replicas: 1	Isr: 1	Elr: 	LastKnownElr:
```
5. Consome latest events in a Kafka topic in Console
```bash
docker exec -it <container_id_or_name> /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> [--from-beginning]
```
