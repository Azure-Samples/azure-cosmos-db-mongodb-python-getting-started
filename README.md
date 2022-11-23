# Azure Cosmos DB API For MongoDB Python Quickstart and Getting Started Guides

This repo shows how to get started with the Azure Cosmos DB API for MongoDB API in a Python application.

* The sample in the root directory, [run.py](run.py), prompts you for connection information. This sample is written with separate functions for each operation as you might do in a production application. Try this sample to get started quickly.

* The sample folders (e.g., **001-quickstart** directory) contain runnable samples used in documentation [quickstart](https://learn.microsoft.com/azure/cosmos-db/mongodb/quickstart-python) and [getting started](https://learn.microsoft.com/azure/cosmos-db/mongodb/how-to-python-get-started) guides. If you make changes here keep the documentation in sync.

The [validate workflow](./github/workflows/validate.yml) is set up for pull requests. See the workflow for tests that are run and run those locally first.

## Sample prerequisites

Prerequisites:

* An Azure Cosmos DB API for MongoDB Account
* Python 3.8+ installed
* [PyMongo](https://www.mongodb.com/docs/drivers/pymongo/) installed
* [python-dotenv](https://pypi.org/project/python-dotenv/) installed to read the connection string from an *.env* file for all samples except the root directory sample.

Use `python run.py` to run the code samples. 

Make sure you define an *.env* variable with the connection string if needed for a sample.