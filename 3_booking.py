import time
import random

import names
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
myclient = MongoClient("mongodb://mongo-admin:admin@34.68.150.66")
# myclient.admin.command('enableSharding', 'test')
# myclient.admin.command('shardCollection', 'test.booking', key={'bookingTime': 1, 'bookingStatus': 1})


# list of system's databases
dblist = myclient.list_database_names()
print(dblist)

# Access database
mydb = myclient["test"]


# list of all collections in your database:
print(mydb.list_collection_names())

################ User Collection #######################
# Access
mycol = mydb["booking"]
mycol.drop()
uscol = mydb["user"]
pkcol = mydb["parkinglot"]
uslist = list(uscol.find({},{"id": 1}))
pklist = list(pkcol.find({},{"id": 1}))


booking_status = ["Failed", "Success", "Processing"]

DocList = []

for i in range(10000):
    Doc = {}
    pairedUs = random.choice(uslist)
    pairedPk = random.choice(pklist)
    # field
    Doc["id"] = str(i)
    Doc["userId"] = pairedUs["id"]
    Doc["prklotId"] = pairedPk["id"]
    Doc["bookingTime"] = time.time()
    Doc["bookingStatus"] = random.choice(booking_status)
    DocList.append(Doc)
    
x= mycol.insert_many(DocList)
print(x.inserted_ids)