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
    print "Usage: dd has no arguments\n"

def dd():
    print "In-Degree Distribution:" 
    result1 = db.in_degree_distribution.find().sort([("$fraction", -1)]).limit(10);
    for r in result1:
        print "Degree = {0}, Fraction = {1}".format(r["_id"], r["fraction"])
    print "\nOut-Degree Distribution:"
    result2 = db.out_degree_distribution.find().sort([("$fraction", -1)]).limit(10);
    for r in result2:
        print "Degree = {0}, Fraction = {1}".format(r["_id"], r["fraction"])
    print "\nAverage Degree:"
    result3 = db.in_degree.aggregate([
            {
                "$group": { "_id": "null", "average": { "$avg": "$degree" } }
            }
        ])
    for r in result3:
        print r["average"]
    # pymongo $avg operator for 'value'
    # Sort by myfield (ascending value) and return first document
    print "\nMinimum Degree:"
    min1 = db.in_degree.find_one(sort=[("degree", 1)])["degree"]
    min2 = db.out_degree.find_one(sort=[("degree", 1)])["degree"]
    if min1 > min2:
        print min2
    else:
        print min1
    print "\nMaximum Degree:"
    max1 = db.in_degree.find_one(sort=[("degree", -1)])["degree"]
    max2 = db.out_degree.find_one(sort=[("degree", -1)])["degree"]
    if max1 > max2:
        print max2
    else:
        print max1
def run(arguments):
    if len(arguments) > 0:
        usage()
        return
    dd()
