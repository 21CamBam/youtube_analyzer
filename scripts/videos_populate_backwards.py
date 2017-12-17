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
videos = db.videos
related_videos = db['related_videos']

DEPTHS = ["depth_three.json"]
raw_data_dir = "/home/csmith2/Dropbox/School Stuff/CS 415/project/data"

for j in range(0, len(DEPTHS)):
    count = 0
    with FileReadBackwards("{0}/{1}".format(raw_data_dir,DEPTHS[j])) as input_file:
        for line in input_file:
            try:
                count += 1
                document = json.loads(line.strip())
                document["rate"] = float(document["rate"])
                print document
                videos.insert_one(document)
            except:
                continue
