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
args = ["x", "y", "target_attr", "descriptive_attr"]
descriptive = ["uploader", "category"]
target = ["age", "length", "views", "rate", "ratings", "comments"]

def usage():
    print "Usage: rangeq x=<integer> y=<integer> target_attr=<string>] [Optional: descriptive_attr=<string>]\n"
    print "Arguments:"
    print "[Required]"
    print "x - lower bound\n"
    print "y - upper bound\n"
    print "target_attr - attribute to be queried against the bounds"
    print "[Optional]"
    print "descriptive_attr - additional query parameter (descriptive_attr=<attribute>,<value>)\n"

def rangeq(x, y, target_attr, descriptive_attr=None):
    if descriptive_attr:
        result = db.videos.find({target_attr: {"$gte": x, "$lt": y}, descriptive_attr[0]: descriptive_attr[1]});
        
        count = 1
        for r in result:
            print r["video_id"] + ", {0} = {1}, {2} = {3}".format(target_attr, r[target_attr], descriptive_attr[0], descriptive_attr[1])
            count += 1
            if count == 20:
                prompt = raw_input("Show 20 more? [y/n]")
                if prompt == 'y':
                    count = 0
                    continue
                else:
                    break
    else:
        result = db.videos.find({target_attr: {"$gte": x, "$lt": y}});
        
        count = 1
        for r in result:
            print r["video_id"] + ", {0} = {1}".format(target_attr, r[target_attr])
            count += 1
            if count == 20:
                prompt = raw_input("Show 20 more? [y/n]")
                if prompt == 'y':
                    count = 0
                    continue
                else:
                    break

def run(arguments):
    x = -1
    y = -1
    target_attr = None
    descriptive_attr = []
    for a in arguments:
        try:
            arg, val = a.split("=")
            if arg not in args:
                ValueError("'{0}' not an accepted argument.".format(arg))
            if arg == 'x':
                x = int(val)
            if arg == 'y':
                y = int(val)
            elif arg == 'target_attr':
                target_attr = val
            elif arg == 'descriptive_attr':
                descriptive_attr = val.split(',')
            else:
                ValueError("'{0}' not an accepted argument.".format(arg))
        except:
            usage()
            return
    if x < 0 or y < 0 or target_attr == None:
        usage()
        return
    print "Entries bounded by [{0},{1}]".format(x,y)
    rangeq(x, y, target_attr, descriptive_attr)
