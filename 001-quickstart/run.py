# -----------------------------------------------------------------------------
#  Prerequisites:
#
# 1. An Azure Cosmos DB API for MongoDB Account.
# 2. PyMongo installed.
# 3. python-dotenv installed (to load environment variables from a .env file).
# -----------------------------------------------------------------------------
# Sample - shows doc CRUD operations oin the Azure Cosmos DB API for MongoDB
#        - for use in quickstart article
# -----------------------------------------------------------------------------

# <package_dependencies>
import os
import sys
from random import randint

import pymongo
from dotenv import load_dotenv

# </package_dependencies>


# <client_credentials>
load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
# </client_credentials>

# <constant_values>
DB_NAME = "adventureworks"
COLLECTION_NAME = "products"
# </constant_values>


def main():
    """Connect to the API for MongoDB, create DB and collection,
    perform CRUD operations
    """

    try:
        # <connect_client>
        client = pymongo.MongoClient(CONNECTION_STRING)
        # </connect_client>
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

    # <new_database>
    # Create database if it doesn't exist
    db = client[DB_NAME]
    if DB_NAME not in client.list_database_names():
        # Create a database with 400 RU throughput that can be shared across
        # the DB's collections
        db.command({"customAction": "CreateDatabase", "offerThroughput": 400})
        print("Created db '{}' with shared throughput.\n".format(DB_NAME))
    else:
        print("Using database: '{}'.\n".format(DB_NAME))
    # </new_database>

    # <create_collection>
    # Create collection if it doesn't exist
    collection = db[COLLECTION_NAME]
    if COLLECTION_NAME not in db.list_collection_names():
        # Creates a unsharded collection that uses the DBs shared throughput
        db.command(
            {"customAction": "CreateCollection", "collection": COLLECTION_NAME}
        )
        print("Created collection '{}'.\n".format(COLLECTION_NAME))
    else:
        print("Using collection: '{}'.\n".format(COLLECTION_NAME))
    # </create_collection>

    # <create_index>
    indexes = [
        {"key": {"_id": 1}, "name": "_id_1"},
        {"key": {"name": 2}, "name": "_id_2"},
    ]
    db.command(
        {
            "customAction": "UpdateCollection",
            "collection": COLLECTION_NAME,
            "indexes": indexes,
        }
    )
    print("Indexes are: {}\n".format(sorted(collection.index_information())))
    # </create_index>

    # <new_doc>
    """Create new document and upsert (create or replace) to collection"""
    product = {
        "category": "gear-surf-surfboards",
        "name": "Yamba Surfboard-{}".format(randint(50, 5000)),
        "quantity": 1,
        "sale": False,
    }
    result = collection.update_one(
        {"name": product["name"]}, {"$set": product}, upsert=True
    )
    print("Upserted document with _id {}\n".format(result.upserted_id))
    # </new_doc>

    # <read_doc>
    doc = collection.find_one({"_id": result.upserted_id})
    print("Found a document with _id {}: {}\n".format(result.upserted_id, doc))
    # </read_doc>

    # <query_docs>
    """Query for documents in the collection"""
    print("Products with category 'gear-surf-surfboards':\n")
    allProductsQuery = {"category": "gear-surf-surfboards"}
    for doc in collection.find(allProductsQuery).sort(
        "name", pymongo.ASCENDING
    ):
        print("Found a product with _id {}: {}\n".format(doc["_id"], doc))
    # </query_docs>


if __name__ == "__main__":
    main()

"""
# <console_result>

Created db 'adventureworks' with shared throughput.

Created collection 'products'.

Indexes are: ['_id_', 'name_1']

Upserted document with _id <ID>

Found a document with _id <ID>:
{'_id': <ID>,
'category': 'gear-surf-surfboards',
'name': 'Yamba Surfboard-50',
'quantity': 1,
'sale': False}

Products with category 'gear-surf-surfboards':

Found a product with _id <ID>:
{'_id': ObjectId('<ID>'),
'name': 'Yamba Surfboard-386',
'category': 'gear-surf-surfboards',
'quantity': 1,
'sale': False}
# </console_result>
"""
