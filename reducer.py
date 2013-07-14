#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
amenity = sys.argv[1]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    data = line.split()
    if amenity == "all" :
	print line
    else :
	if amenity == data[1].split(':')[0] :
		print line
   
