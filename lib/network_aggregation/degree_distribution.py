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

def dd():
    print "In-Degree Distribution:"
    # map function: given video_id x, find all documents with video_id2 = x
    # reduce function: for each key, return count(values)
    # reduce function #2: for each distinct degree d (key) in the previous query results, count(all documents with degree d)/count(all documents)
    # sort final query
    # print highest 14 degrees and 15+ = sum(rest of the degree values)
    print "Out-Degree Distribution:" # All 20
    # map function: given video_id x, find all documents with video_id1 = x
    # reduce function: for each key, return count(values)
    # reduce function #2: for each distinct degree d (key) in the previous query results, count(all documents with degree d)/count(all documents)
    # sort final query
    # print highest 14 degrees and 15+ = sum(rest of the degree values)
    print "Average Degree:"
    # pymongo $avg operator for 'value'
    # Sort by myfield (ascending value) and return first document
    print "Minimum Degree:"
    #result.find_one(sort=[("value", 1)])["value"]
    print "Maximum Degree:"
    #result.find_one(sort=[("value", -1)])["value"]
