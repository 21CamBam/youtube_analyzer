import os
import pymongo
import json

from bson.code import Code
from pymongo import MongoClient

# MongoDB Setup
client = MongoClient()
client = MongoClient('mongodb://cammi:6985.bQoLX*3935@youtubeanalyzer-shard-00-00-2lnvs.mongodb.net:27017,youtubeanalyzer-shard-00-01-2lnvs.mongodb.net:27017,youtubeanalyzer-shard-00-02-2lnvs.mongodb.net:27017/youtube_analyzer?ssl=true&replicaSet=YoutubeAnalyzer-shard-0&authSource=admin')

db = client.youtube_analyzer
videos = db.related_videos

def pgr(k):
    # map function: given video_id x, find all documents with video_id2 = x
    # reduce function: for each key, return count(values) + 10 since all videos have a degree of at least 10 as degree
    # sort final query
    count = 1
    for r in result.find():
        print count + ". " + r["video_id2"]
        count += 1
        if (count == k):
            break
    
def run(arguments):
    pass
