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
    """Connect to the API for MongoDB and drop database."""

    try:
        load_dotenv()
        CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
        client = pymongo.MongoClient(CONNECTION_STRING)

        # <drop_database>
        DB_NAME = input("Enter database name to drop: ")
        if DB_NAME in client.list_database_names():
            print("Dropping database: {}".format(DB_NAME))
            client.drop_database(DB_NAME)
        else:
            print("Didn't find database: {}".format(DB_NAME))
        # </drop_database>

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
Enter database name to drop: adventureworks
Dropping database: adventureworks
# </console_result>
"""
