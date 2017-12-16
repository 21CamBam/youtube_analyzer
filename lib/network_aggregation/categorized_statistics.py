import os
import pymongo
import json

from bson.code import Code
from pymongo import MongoClient

# MongoDB Setup
client = MongoClient()
client = MongoClient('mongodb://cammi:6985.bQoLX*3935@youtubeanalyzer-shard-00-00-2lnvs.mongodb.net:27017,youtubeanalyzer-shard-00-01-2lnvs.mongodb.net:27017,youtubeanalyzer-shard-00-02-2lnvs.mongodb.net:27017/youtube_analyzer?ssl=true&replicaSet=YoutubeAnalyzer-shard-0&authSource=admin')

db = client.youtube_analyzer
videos = db.videos

descriptive = ["uploader", "category"]
target = ["age", "length", "views", "rate", "ratings", "comments"]

def cstat(attr, value):
    count = 0
    count = db.videos.find({attr: value})
    print "Number of videos where {0} is {1}: {2}".format(attr, value, count)
    
def run(arguments):
    pass
