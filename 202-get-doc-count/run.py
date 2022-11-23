# ----------------------------------------------------------------------------
#  Prerequisites:
#
# 1. An Azure Cosmos DB API for MongoDB Account.
# 2. PyMongo installed.
# 3. python-dotenv installed (to load environment variables from a .env file).
# ----------------------------------------------------------------------------
# Code samples are used in documentation, keep synchronized with docs.
# ----------------------------------------------------------------------------

import os
import sys

import pymongo
from dotenv import load_dotenv


def main():
    """Connect to the API for MongoDB and get document count."""

    try:
        load_dotenv()
        CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
        client = pymongo.MongoClient(CONNECTION_STRING)

        # <database_object>
        # Get list of databases
        databases = client.list_database_names()

        # Loop through databases
        for db in databases:
            print("Database: {}".format(db))

            # Get list of collections
            collections = client[db].list_collection_names()

            # Loop through collections
            for col in collections:
                print("\tCollection: {}".format(col))

                # Get document count
                doc_count = client[db][col].count_documents({})
                print("\tDocument count: {}".format(doc_count))
        # </database_object>

        try:
            client.server_info()  # validate connection string
        except (
            pymongo.errors.OperationFailure,
            pymongo.errors.ConnectionFailure,
            pymongo.errors.ExecutionTimeout,
        ) as err:
            sys.exit("Can't connect:" + str(err))
    except Exception as err:
        sys.exit("Error:" + str(err))

    client.close()


if __name__ == "__main__":
    main()

"""
# <console_result>
Database: adventureworks
        Collection: products_new
        Document count: 1
        Collection: products
        Document count: 3
Database: testdb
        Collection: mycoll
        Document count: 1
# </console_result>
"""
