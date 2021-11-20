import random

import names
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
myclient = MongoClient("mongodb://mongo-admin:admin@34.68.150.66")
# myclient.admin.command('enableSharding', 'test')
# myclient.admin.command('shardCollection', 'test.parkinglot', key={'prkStatus': 1, 'prkLoc': 1})


# list of system's databases
dblist = myclient.list_database_names()
print(dblist)

# Access database
mydb = myclient["test"]


# list of all collections in your database:
print(mydb.list_collection_names())

################ User Collection #######################
# Access
mycol = mydb["parkinglot"]
mycol.drop()

DocList = []

for i in range(1000):
    Doc = {}
    Doc["id"] = str(i)
    Doc["prkInfo"] = names.get_first_name() + " Parking"
    Doc["prkStatus"] = random.randint(0, 100)
    Doc["prkLoc"] = {"lat": random.uniform(10.7,10.8), "long": random.uniform(106.6,106.7)}
    DocList.append(Doc)

x= mycol.insert_many(DocList)
print(x.inserted_ids)