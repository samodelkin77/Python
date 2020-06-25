from nosqldb import ConnectionException
from nosqldb import Factory
from nosqldb import StoreConfig

import logging
import sys


storeHost = 'tpaprod-ldbxe01'
storePort = 5000
storeName = 'kvstore'

# kvstoreconfig = StoreConfig('kvstore', [storeHost])
# store = Factory.open ()

def open_store():
    try:
        kvstoreconfig = StoreConfig('kvstore', [storeHost + ':' + str(storePort)])
        return Factory.open(proxy, kvstoreconfig)
    except ConnectionException as ce:
        logging.error("Store connection failed.")
        logging.error(ce.message)
        sys.exit(-1) 

store = open_store()
store.close()


