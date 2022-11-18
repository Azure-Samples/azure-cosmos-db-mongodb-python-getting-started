# ------------------------------------------------------------------------------
#  Prerequisites:
#
# 1. An Azure Cosmos DB API for MongoDB Account.
# 2. PyMongo installed.
# 3. python-dotenv installed (to load environment variables from a .env file).
# ------------------------------------------------------------------------------
# Code samples are used in documentation, keep synchronized with documentation.
# ------------------------------------------------------------------------------

# <package_dependencies>
import os
import sys

import pymongo
from dotenv import load_dotenv

# </package_dependencies>


def main():
    """Connect to the API for MongoDB"""

    try:
        # <client_credentials>
        load_dotenv()
        CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
        client = pymongo.MongoClient(CONNECTION_STRING)

        for prop, value in vars(client.options).items():
            print("Property: {}: Value: {} ".format(prop, value))
        # </client_credentials>
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
Property: _ClientOptions__options: Value:
{'replicaSet': 'globaldb', 'retrywrites': False, 'maxIdleTimeMS': 120.0,
'appName': '@cosmosdb-mongodb@', 'document_class': <class 'dict'>,
'tz_aware': False, 'connect': True, 'tls': True}
Property: _ClientOptions__codec_options: Value:
CodecOptions(document_class=dict, tz_aware=False,
uuid_representation=UuidRepresentation.UNSPECIFIED,
unicode_decode_error_handler='strict', tzinfo=None,
type_registry=TypeRegistry(type_codecs=[], fallback_encoder=None),
datetime_conversion=DatetimeConversion.DATETIME)
Property: _ClientOptions__direct_connection: Value: None
Property: _ClientOptions__local_threshold_ms: Value: 15
Property: _ClientOptions__server_selection_timeout: Value: 30
Property: _ClientOptions__pool_options: Value:
  <pymongo.pool.PoolOptions object at 0x0000013AC16A9170>
Property: _ClientOptions__read_preference: Value: Primary()
Property: _ClientOptions__replica_set_name: Value: globaldb
Property: _ClientOptions__write_concern: Value: WriteConcern()
Property: _ClientOptions__read_concern: Value: ReadConcern()
Property: _ClientOptions__connect: Value: True
Property: _ClientOptions__heartbeat_frequency: Value: 10
Property: _ClientOptions__retry_writes: Value: False
Property: _ClientOptions__retry_reads: Value: True
Property: _ClientOptions__server_selector: Value:
  <function any_server_selector at 0x0000013AC104F490>
Property: _ClientOptions__auto_encryption_opts: Value: None
Property: _ClientOptions__load_balanced: Value: None
Property: _ClientOptions__timeout: Value: None
# </console_result>
"""
