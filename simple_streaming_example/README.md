# Pyspark Streaming Jupyter Tutorial
Tutorial for Pyspark Structured Streaming with Kafka + Jupyter

## Prerequisites
1. Install [Java 21](https://www.oracle.com/il-en/java/technologies/downloads/#java21).  
Java JRE is required to work well with PySpark. 

Make sure JAVA_HOME is set:
```bash
echo $JAVA_HOME
```

# Setup 
## (1) Setup Jupyter:
1. Check your Python Version. Obtain 3.11 version (or any version that is compatible with PySpark4.1 Structure Streaming)
```bash
python --version
```
2. Open Python venv
```bash
python3.11 -m venv .venv3.11
source .venv3.11/bin/activate
```

change to directory you already created: pyspark
```bash
cd ~/pyspark
```

3. Install jupyter package
```bash
pip install jupyter
```
4. Run Jupyter
For local machine, run:
```bash
jupyter notebook 
```
A browser will be opened.

If you run on local PC, skip to step 5.

In case you run linux on EC2 virtual machine and not on your local PC, you will need to forward the browser to your local machine.
run:
```bash
jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser
```
then open the broser with the url http://<your_buclic_ec2_ip>:8888
The UI will prompt for a token. Obtain the token from the console output

5. Open a notebook
- In the web console that opens, open a new notebook of Python 3
6. Run the notebook (Note that you need Docker and Kafka broker running. See below)
- Use the Notebook [pyspark_structured_streaming_wikimedia.ipynb.ipynb](https://github.com/ransilberman/pyspark-streaming-jupyter-tutorial/blob/main/simple_streaming_example/pyspark_structured_streaming_wikimedia.ipynb.ipynb)

## (2) Setup Docker
Install and run docker on your PC in order to run Kafka container

See [Get Started with Docker](https://www.docker.com/get-started/)

## (3) Setup Kafka
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
# Lookup Kafka Topics
After Kafka is running and after data was sent to a Kafka topic, you can see its content:
1. Run the following command to list Kafka topics:
```bash
docker exec -it <container_id_or_name> /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```
Result may look like the following:
```bash
wikimedia_topic_1
```
2. Describe a certain topic:
```bash
docker exec -it <container_id_or_name> /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic <topic_name>
```
Result may look like this:
```bash
Topic: wikimedia_topic_1	TopicId: 1PFZVJkIT9ex7Cx-AycgtA	PartitionCount: 1	ReplicationFactor: 1	Configs: segment.bytes=1073741824
	Topic: wikimedia_topic_1	Partition: 0	Leader: 1	Replicas: 1	Isr: 1	Elr: 	LastKnownElr:
```
3. Consome latest events in a Kafka topic in Console
```bash
docker exec -it <container_id_or_name> /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> [--from-beginning]
```
