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
    """Connect to the API for MongoDB and show admin commands"""

    try:
        load_dotenv()
        CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
        client = pymongo.MongoClient(CONNECTION_STRING)

        # <server_info>
        # Get server information
        for k, v in client.server_info().items():
            print("Key: {} , Value: {}".format(k, v))

        # Get server status of admin database
        print("Server status {}".format(client.admin.command("serverStatus")))

        # List databases
        databases = client.list_database_names()
        print("Databases: {}".format(databases))
        # </server_info>

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

    # <client_disconnect>
    client.close()
    # </client_disconnect>


if __name__ == "__main__":
    main()

"""
# <console_result>

# </console_result>
"""
