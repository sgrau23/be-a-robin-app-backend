from pymongo import MongoClient
from src.utils import get_settings

# Obtain settings
SETTINGS = get_settings('db')

# Declare global DB variables
DB = None
COLLECTIONS = {}


def initialize_db():
    global DB
    DB = MongoClient(SETTINGS['mongo_db_uri'], SETTINGS['port'])[SETTINGS['db_name']]


def initialize_collections():
    global COLLECTIONS
    for router_key, collections_list in SETTINGS['collections'].items():
        collections_instances = {}
        for collection_name in collections_list:
            collections_instances[collection_name] = DB[collection_name]
        COLLECTIONS[router_key] = collections_instances
