import datetime
import lib.influence_analysis.pagerank as pagerank
import lib.network_aggregation.categorized_statistics as categorized_statistics
import lib.network_aggregation.degree_distribution as degree_distribution
import lib.search.range_queries as range_queries
import lib.search.top_kqueries as top_kqueries
import time
import bson

# CLI Setup
verbose = "\
dd     - degree distribution (no arguments)\n\
cstat  - categorical statistics (one required argument)\n\
topk   - top k queries (one required and two optional arguments)\n\
rangeq - range queries (three required and one optional arguments)\n\
pgr    - pagerank influence analysis (no arguments)\n\
help   - list commands (no arguments)\n"

def print_commands(v):
    if len(v) > 0:
        if v[0] == 'verbose' or v[0] == 'v':
            print verbose
            return
        print v[0]
        print "Usage: help [Optional: verbose or v]"
    else:
        print "    ".join(commands.keys())
        
commands = {
    "dd": degree_distribution.run,
    "cstat": categorized_statistics.run,
    "topk": top_kqueries.run,
    "rangeq": range_queries.run,
    "pgr": pagerank.run,
    "help": print_commands
}

def main():
    print "youtube_analyzer shell v1.0"
    print "Welcome to Cammi's YouTube Dataset Analysis Tool!"
    while(1):
        cmd = raw_input("> ")
        elements = cmd.strip().split()
        if not any([cmd.startswith(s) for s in commands.keys()]):
            print "Invalid command. Acceptable commands are: {0}".format(", ".join(commands))
            continue
        start_time = time.time()
        commands[elements[0].strip()](elements[1:])
        print("--- Runtime: %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
