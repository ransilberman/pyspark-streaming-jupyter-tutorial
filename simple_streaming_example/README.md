# Pyspark Streaming Jupyter Tutorial
Tutorial for Pyspark Structured Streaming with Kafka + Jupyter

## Setup
1. Check your Python Version
```bash
python3.6 --version
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
pip install pyspark
pip install findspark
pip install requests
pip install sseclient
```
4. Find the full path of PySpark Home directrory
Open python console by typing 'python3', then:
```python
import pyspark
print(pyspark.__file__)
print(pyspark.__version__)
```
The result may look like this:
```
/Users/myuser/projects/pyspark/.venv/lib/python3.11/site-packages/pyspark/__init__.py
3.5.4
```
- Copy the string without the module name `__init__.py` to use as the `SPARK_HOME`
- Copy the pyspark version
5. Run Jupyter
For local machine, run:
```bash
jupyter-notebook 
```
A browser will be opened.

For EC2 virtual machine, run:
```bash
jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser
```
then open the broser with the url http://<your_buclic_ec2_ip>:8888
The UI will prompt for a token. Obtain the token from the console output
6. Open a notebook
- In the web console that opens, open a new notebook of Python 3
7. Test a demo notebook
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
