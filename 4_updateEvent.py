import time
import random

import names
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
myclient = MongoClient("mongodb://mongo-admin:admin@34.68.150.66")
# myclient.admin.command('enableSharding', 'test')
# myclient.admin.command('shardCollection', 'test.updateEvent', key={'rqTime': 1})


# list of system's databases
dblist = myclient.list_database_names()
print(dblist)

# Access database
mydb = myclient["test"]


# list of all collections in your database:
print(mydb.list_collection_names())

################ User Collection #######################
# Access
mycol = mydb["updateEvent"]
mycol.drop()
pkcol = mydb["parkinglot"]
pklist = list(pkcol.find({},{"id": 1, "prkLoc": 1}))

DocList = []

for i in range(10000):
    Doc = {}
    pairedPk = random.choice(pklist)
    Doc["id"] = str(i)
    Doc["prkID"] = pairedPk["id"]
    Doc["rqTime"] = time.time()
    Doc["prkLoc"] = pairedPk["prkLoc"]
    DocList.append(Doc)
    
x= mycol.insert_many(DocList)
print(x.inserted_ids)