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

def usage():
    print "Usage: topk k=<integer> [Optional: sort_paramater=<string>] [Optional: attr=<string>]\n"
    print "Arguments:"
    print "[Required]"
    print "k - number of results to print\n"
    print "[Optional]"
    print "sort_parameter - the attribute to be printed"
    print "attr - the attribute by which rank the top values"

def topk(k=10, sort="uploader", attr=["video_id"]):
    map = Code("function () {"
                "  this.{0}.forEach(function(z) {"
                "    emit(z, 1);"
                "  });"
                "}".format(sort))         
    reduce = Code("function (key, values) {"
                   "  var total = 0;"
                   "  for (var i = 0; i < values.length; i++) {"
                   "    total += values[i];"
                   "  }"
                   "  return total;"
                   "}")
    result = db.videos.map_reduce(map, reduce, "myresults")
    result.sort("value", 1)
    
    count = 1
    for r in result.find():
        print count + ". " + r[sort]
        count += 1
        if (count == k):
            break

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
        attr = 'video_id'
    print "Top {0} {1}'s with the most {2}s".format(k,sort,attr)
    topk(k, sort, attr)
