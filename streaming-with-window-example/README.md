# Pyspark Streaming With Window Functions
Tutorial for Pyspark Structured Streaming with Window Operations

## Setup
1. Follow Setup from simple_streaming_example/pyspark_structured_streaming.ipynb [simple_streaming_example/README.md](https://github.com/ransilberman/pyspark-streaming-jupyter-tutorial/blob/main/simple_streaming_example/README.md)

## Run Kafka
1. Start Kafka container as described in simple_streaming_example/pyspark_structured_streaming.ipynb
2. Open a new Commandline Console and set virtual environment and all needed pip installed as done in the Setup phase
3. In the new console, run a KafkaProducer program that reads Wikimedia changes and writes them to Kafka topic
Python code is found here: [wikimedia_stream.py](https://github.com/ransilberman/pyspark-streaming-jupyter-tutorial/blob/main/streaming-with-window-example/wikimedia_stream.py)

## Open Jupiter
1. Run Jupyter
```bash
jupyter-notebook
```
2. Open a new notebook
- In the web console that opens, open a new notebook of Python 3
3. Test a demo notebook
- Copy the content of the file [streaming_window.ipynb](https://github.com/ransilberman/pyspark-streaming-jupyter-tutorial/blob/main/streaming-with-window-example/streaming_window.ipynb)
- Replace the `SPARK_HOME` value with the SPARK_HOME as in previous module.
- Replace the PYSPARK_VERSION with the version you obtained in previous version
- Start running the notebook

