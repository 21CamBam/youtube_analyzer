import os
import pymongo
import json

from pymongo import MongoClient

# MongoDB Setup
client = MongoClient()
client = MongoClient('mongodb+srv://cammi:6985.bQoLX*3935@youtubeanalyzer-21nvs.mongodb.net/test')

db = client.youtube_analyzer

def topk(k=10, sort="uploader", attr=["video_id"]):
    
