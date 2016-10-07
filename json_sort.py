import sys
import json

class JsonSort:
    """"""

if len(sys.argv) < 2:
    print "Usage : json_sort.py <json file>"
    exit(1)

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)
    print data