# ----------------------------------------------------------------------------------------------------------
#  Prerequisites:
#
# 1. An Azure Cosmos DB API for MongoDB Account.
# 2. PyMongo installed.
# 3. python-dotenv installed (to load environment variables from a .env file).
# ----------------------------------------------------------------------------------------------------------
# Sample - demonstrates the basic CRUD operations on a document in the Azure Cosmos DB API for MongoDB
#        - for use in quickstart article
# ----------------------------------------------------------------------------------------------------------

# <package_dependencies>
import os
import sys
import pymongo
from dotenv import load_dotenv
from random import randint
# </package_dependencies>


# <client_credentials>
load_dotenv()
CONNECTION_STRING = os.environ.get('COSMOS_CONNECTION_STRING')
# </client_credentials>

# <constant_values>
DB_NAME = "adventureworks"
COLLECTION_NAME = "products"
SAMPLE_FIELD_NAME = "name"
# </constant_values>

def main():
    """Connect to the API for MongoDB, create DB and collection, perform CRUD operations"""

    try:
        # <connect_client>
        client = pymongo.MongoClient(CONNECTION_STRING)
        # </connect_client>
        try:
            client.server_info() # validate connection string
            print ("Connected to MongoDB successfully!\n")
        except (pymongo.errors.OperationFailure,
                pymongo.errors.ConnectionFailure,
                pymongo.errors.ExecutionTimeout) as err:
            sys.exit("Can't connect:" + str(err))
    except Exception as err:
        sys.exit("Error:" + str(err))

    # <new_database>
    # Database reference with creation on first write if it doesn't already exist
    db = client[DB_NAME]
    print("Using database: {}\n".format(DB_NAME))
    # </new_database>

    # <create_collection>
    # Collection reference with creation on first write if it doesn't already exist
    collection = db[COLLECTION_NAME]
    print("Using collection: {}\n".format(COLLECTION_NAME))
    # </create_collection>

    # <create_index>
    result = collection.create_index([('name', pymongo.ASCENDING)], unique=True)
    print("Indexes are: {}\n".format(sorted(collection.index_information())))
    # </create_index>

    # <new_doc>
    """Create new document and upsert (create or replace) to collection"""
    product = {
        'category': 'gear-surf-surfboards',
        'name': 'Yamba Surfboard-{}'.format(randint(50, 5000)),
        'quantity': 1,
        'sale': False
    }
    result = collection.update_one(
        {'name': product['name']},
        {'$set': product}, 
        upsert=True)
    print("Upserted document with _id {}\n".format(result.upserted_id))
    # </new_doc>

    # <read_doc>
    doc = collection.find_one({"_id": result.upserted_id})
    print("Found a document with _id {}: {}\n".format(result.upserted_id, doc))
    # </read_doc>

    # <query_docs>
    """Query for documents in the collection"""
    print("Products with category 'gear-surf-surfboards':\n")
    allProductsQuery = {
        "category": "gear-surf-surfboards"
    } 
    for doc in collection.find(allProductsQuery).sort('name', pymongo.ASCENDING):
        print("Found a product with _id {}: {}\n".format(doc["_id"], doc))
    # </query_docs>

if __name__ == '__main__':
    main()

"""
# <console_result>
Using database: adventureworks

Using collection: products

Indexes are: ['_id_', 'name_1']

Upserted document with _id <ID>

Found a document with _id <ID>: {'_id': <ID>, 'category': 'gear-surf-surfboards', 'name': 'Yamba Surfboard-50', 'quantity': 1, 'sale': False}

Products with category 'gear-surf-surfboards':

Found a product with _id <ID>: {'_id': ObjectId('<ID>'), 'name': 'Yamba Surfboard-386', 'category': 'gear-surf-surfboards', 'quantity': 1, 'sale': False}
# </console_result>
"""