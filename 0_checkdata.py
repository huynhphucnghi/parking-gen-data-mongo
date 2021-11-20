from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
myclient = MongoClient("mongodb://mongo-admin:admin@34.68.150.66")
# db=myclient.admin
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)


# list of system's databases
dblist = myclient.list_database_names()
print("DB list:", dblist)

# Access database
mydb = myclient["test"]
# list of all collections in your database:
print("Collections: ", mydb.list_collection_names())

################ User Collection #######################
# Access
print("User Collection")
mycol = mydb["user"]
for x in mycol.find():
    print(x)

print("Parkinglot Collection")
mycol = mydb["parkinglot"]
for x in mycol.find():
    print(x)


