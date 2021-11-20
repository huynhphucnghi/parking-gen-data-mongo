import time
import random

from pymongo import MongoClient
# connect to MongoDB
myclient = MongoClient("mongodb://mongo-admin:admin@34.68.150.66")
myclient.admin.command('enableSharding', 'test_sharded')
myclient.admin.command('shardCollection', 'test_sharded.user', key={'rstTime': 1})
myclient.admin.command('shardCollection', 'test_sharded.parkinglot', key={'prkStatus': 1, 'prkLoc': 1})
myclient.admin.command('shardCollection', 'test_sharded.booking', key={'bookingTime': 1, 'bookingStatus': 1})
myclient.admin.command('shardCollection', 'test_sharded.updateEvent', key={'rqTime': 1})