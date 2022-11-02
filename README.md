# Azure Cosmos DB API For MongoDB Python Quickstart

Thi repo shows how to get started with the Azure Cosmos DB API for MongoDB API in a Python application. There are two samples.

* The sample in the root directory, [run.py](run.py), prompts you for connection information. This sample is written with separate functions for each operation as you might do in a production application.

* The sample in the **001-quickstart** directory, [001-quickstart/run.py](/001-quickstart/run.py), reads an environment variable, creates an AdventureWorks collection, and creates an index. The second sample provides code snippets for the related quickstart: https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/quickstart-python and is structured for simplicity.

## Sample 1

Prerequisites:

* An Azure Cosmos DB API for MongoDB Account
* Python 3.8+ installed
* [PyMongo](https://www.mongodb.com/docs/drivers/pymongo/) installed

Use `python run.py` to run the code which will prompt you for a connection string.

### Sample 2 - Quickstart documentation

The quickstart https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/quickstart-python uses the code snippets from the *001-quickstart/run.py* file and sets connection string information in an *.env* file.

Prerequisites:

* An Azure Cosmos DB API for MongoDB Account
* Python 3.8+ installed
* [PyMongo](https://www.mongodb.com/docs/drivers/pymongo/) installed
* [python-dotenv](https://pypi.org/project/python-dotenv/) installed to read the connection string from an *.env* file

**Step 1.** Copy the *001-quickstart/.env.sample* file to *001-quickstart/.env* and fill in the connection information.

**Step 2.** From the root directory, run `python 001-quickstart/run.py`.
