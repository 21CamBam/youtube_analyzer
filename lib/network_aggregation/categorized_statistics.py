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

args = {"uploader": str, "category":str, "video_age":int, "video_length":int, "num_views":int, "rate":float, "num_ratings":int, "num_comments":int}

def usage():
    print "Usage: cstat field1=val1 field2=val2...\n"

def cstat(doc):
    count = db.videos.find(doc).count()
    print "Number of videos that satisfy {0}: {1}".format(doc, count)

def run(arguments):
    doc = {}
    for a in arguments:
        try:
            key, val = a.strip().split('=')
            if key not in args.keys():
                usage()
                return
            doc[key] = args[key](val)
        except:
            usage()
            return
    cstat(doc)
