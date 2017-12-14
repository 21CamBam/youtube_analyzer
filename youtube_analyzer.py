import datetime
import pymongo
import lib.influence_analysis.pagerank as pagerank
import lib.network_aggregation.categorized_statistics as categorized_statistics
import lib.network_aggregation.gegree_distribution as degree_distribution
import lib.search.range_queries as range_queries
import lib.search.recognition_patterns as recognition_patterns
import lib.search.top_kqueries as top_kqueries

from pymongo import MongoClient

# MongoDB Setup
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')

db = client['youtube-database']

videos = db['test-collection']
related_videos = db['test-collection']

# CLI Setup
commands = {
    "dd": degree_distribution.run,
    "cstat": categorized_statistics.run,
    "topk": top_kqueries.run,
    "rangeq": range_queries.run,
    "userpattern": pattern_recognition.run,
    "pgr": pagerank.run
}

def do_run(cmd):
    tokens = cmd.split()
    

def main():
    while(1):
        cmd = input("> ")
        if not any([cmd.startswith(s) for s in commands.keys()]):
            print "Invalid command. Acceptable commands are: {0}".format(", ".join(commands))
        do_run(cmd)

if __name__ == "__main__":
    main()
