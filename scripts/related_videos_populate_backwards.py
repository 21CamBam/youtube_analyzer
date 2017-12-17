import os
import json
import pymongo
import sys

from file_read_backwards import FileReadBackwards

from pymongo import MongoClient

# MongoDB Setup
try:
    client = pymongo.MongoClient('mongodb://cammi:6985.bQoLX*3935@youtubeanalyzer-shard-00-00-2lnvs.mongodb.net:27017,youtubeanalyzer-shard-00-01-2lnvs.mongodb.net:27017,youtubeanalyzer-shard-00-02-2lnvs.mongodb.net:27017/youtube_analyzer?ssl=true&replicaSet=YoutubeAnalyzer-shard-0&authSource=admin')
except:
    print "Connection to mongoDB failed..."
    sys.exit(1)

#db = client['youtube_analyzer']
db = client["youtube_analyzer"]
related_videos = db['related_videos']

raw_data_dir = "/home/csmith2/Dropbox/School Stuff/CS 415/project/youtube_data/related_videos.json"

with FileReadBackwards(raw_data_dir, encoding="utf-8") as input_file:
    for line in input_file:
        try:
            document = json.loads(line.strip())
            print document
            related_videos.insert_one(document)
        except:
            continue
