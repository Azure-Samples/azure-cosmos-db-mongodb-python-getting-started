# Azure Cosmos DB API For MongoDB Python Quickstart and Getting Started Guides

Thi repo shows how to get started with the Azure Cosmos DB API for MongoDB API in a Python application.

* The sample in the root directory, [run.py](run.py), prompts you for connection information. This sample is written with separate functions for each operation as you might do in a production application. Try to the sample to get started quickly.

* The sample folders (e.g., **001-quickstart** directory) contain runnable samples used in documentation https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/quickstart-python.

## Sample prerequisites

Prerequisites:

* An Azure Cosmos DB API for MongoDB Account
* Python 3.8+ installed
* [PyMongo](https://www.mongodb.com/docs/drivers/pymongo/) installed
* [python-dotenv](https://pypi.org/project/python-dotenv/) installed to read the connection string from an *.env* file for all samples outside the root sample.

Use `python run.py` to run the code which will prompt you for a connection string.

Make sure you define an *.env* variable with the connection string if needed for a sample.