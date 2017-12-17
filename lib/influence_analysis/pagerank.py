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

def usage():
    print "Usage: pgr has no arguments\n"

def pgr():
    result1 = db["in_degree"].find().sort([("degree", -1)]).limit(50) # top 20 most influential videos
    count = 0
    d = []
    print "{:5} {:12} {:16} {:24} {:10} {:10} {:10} {:10} {:10}".format("Rank", "Video ID", "Uploader", "Category", "Age", "Length", "Views", "Rate", "Ratings", "Comments")
    for r in result1:
        if count == 20:
            return
        try:
            result = db.videos.find_one({"video_id": r["_id"]})
            if result in d:
                continue
            d.append(result["video_id"])
            count += 1
            for f in result:
                print "{:5} {:12} {:16} {:24} {:10} {:10} {:10} {:10} {:10}".format(str(count), result["video_id"], result["uploader"], result["category"], str(result["video_age"]), str(result["video_length"]), str(result["num_views"]), str(result["rate"]), str(result["num_ratings"]), str(result["num_comments"]))
                break
        except:
            continue
            
def run(arguments):
    if len(arguments) > 0:
        usage()
        return
    pgr()
