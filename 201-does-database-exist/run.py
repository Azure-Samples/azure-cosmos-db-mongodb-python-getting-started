# ----------------------------------------------------------------------------------------------------------
#  Prerequisites:
#
# 1. An Azure Cosmos DB API for MongoDB Account.
# 2. PyMongo installed.
# 3. python-dotenv installed (to load environment variables from a .env file).
# ----------------------------------------------------------------------------------------------------------
# Code samples are used in documentation, do not change unless synchronizing with documentation.
# ----------------------------------------------------------------------------------------------------------

import os
import sys

import pymongo
from dotenv import load_dotenv


def main():
    """Connect to the API for MongoDB and check if database exists"""

    try:
        load_dotenv()
        CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
        client = pymongo.MongoClient(CONNECTION_STRING)

        # <does_database_exist> 
        # Get list of databases
        databases = client.list_database_names()
        if not databases:
            print("No databases found")

        # Does database exist?
        DB_NAME = "adventureworks2"
        if DB_NAME in client.list_database_names():
            print("Database exists: {}".format(DB_NAME))
        else:
            client[DB_NAME].command({"customAction": "CreateDatabase", "offerThroughput": 400})
            print("Created db '{}' with shared throughput.\n".format(DB_NAME))
        # </does_database_exist>

        # <does_collection_exist>
        COLL_NAME = "products2"
        if COLL_NAME in client[DB_NAME].list_collection_names():
            print("Collection exists: {}".format(COLL_NAME))
        else:
            client[DB_NAME].command({"customAction": "CreateCollection", "collection": COLL_NAME})
            print("Created collection '{}'.\n".format(COLL_NAME))
        # </does_collection_exist>

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
Database exists: adventureworks
# </console_result>
"""
