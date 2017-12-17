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

args = ["k", "sort_parameter", "attr"]

attrs2 = {
    "video_age": "function () {\
                    emit(this.uploader, this.age);\
              }",
    "video_length": "function () {\
                    emit(this.uploader, this.length);\
              }",
    "num_views": "function () {\
                    emit(this.uploader, this.views);\
              }",
    "rate": "function () {\
                    emit(this.uploader, this.rate);\
              }",
    "num_ratings": "function () {\
                    emit(this.uploader, this.ratings);\
              }",
    "num_comments": "function () {\
                    emit(this.uploader, this.comments);\
              }"
}

def usage():
    print "Usage: topk k=<integer> [Optional: sort_paramater=<string>] [Optional: attr=<string>]\n"
    print "Arguments:"
    print "[Required]"
    print "k - number of results to print\n"
    print "[Optional]"
    print "sort_parameter - the attribute to be printed"
    print "attr - the attribute by which rank the top values\n"

def topk(k=10, sort="video_id", attr=["num_views"]):
    if attr == "video_id":
        result = db.most_uploaded.find().limit(k)
        
        count = 1
        sort = "_id"
        for r in result:
            print str(count) + ". " + r[sort] + ", Videos uploaded = {0}".format(r["count"])
            count += 1
    else:
        result = db.videos.find().sort([(attr, -1)]).limit(k);
        count = 1
        for r in result:
            print str(count) + ". " + r[sort] + ", {0} = {1}".format(attr, r[attr])
            count += 1

def run(arguments):
    k = -1
    sort = None
    attr = None
    for a in arguments:
        try:
            arg, val = a.split("=")
            if arg not in args:
                ValueError("'{0}' not an accepted argument.".format(arg))
            if arg == 'k':
                k = int(val)
            elif arg == 'sort_parameter':
                sort = val
            elif arg == 'attr':
                attr = val
            else:
                ValueError("'{0}' not an accepted argument.".format(arg))
        except:
            usage()
            return
    if k < 0:
        usage()
        return
    if attr == 'video_id' or sort == None:
        sort = 'uploader'
    if attr == None:
        attr = 'num_views'
    print "Top {0} {1}'s with the most {2}s".format(k,sort,attr)
    topk(k, sort, attr)
