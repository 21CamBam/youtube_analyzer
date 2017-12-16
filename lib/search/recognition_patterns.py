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

def sp(search_attrs):
    # search for all videos related to all search_attrs
    # input: node1->node2,node2->node3,node3->node1
    if descriptive_attr:
        pre_res = db.videos.create_index([(descriptive_attr, pymongo.ASCENDING)], unique=True)
    else:
        # result = range query over pre_res
        for r in result.find():
            print r["video_id"]
