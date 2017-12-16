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

def rangeq(x, y, target_attr, descriptive_attr=None):
    if descriptive_attr:
        pre_res = db.videos.create_index([(descriptive_attr, pymongo.ASCENDING)], unique=True)
    else:
        # result = range query over pre_res
        for r in result.find():
            print r["video_id"]
    
def run(arguments):
    pass
