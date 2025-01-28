# Pyspark Streaming Jupyter Tutorial
Tutorial for Pyspark Structured Streaming with Kafka + Jupyter

## Setup
1. Check your Python Version
```bash
python3.6 --version
```
2. Open Python venv
```bash
python3.6 -m venv .venv3.6
source .venv3.6/bin/activate
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
```bash
jupyter-notebook
```
6. Open a notebook
- In the web console that opens, open a new notebook of Python 3
7. Test a demo notebook
- Copy the content of the file [pyspark_structured_streaming.ipynb](https://github.com/ransilberman/pyspark-streaming-jupyter-tutorial/blob/main/pyspark_structured_streaming.ipynb)
- Replace the `SPARK_HOME` value with the SPARK_HOME that you obtained in step #4.
- Replace the PYSPARK_VERSION with the version you obtained above

