#!/usr/bin/env python
import sys
import os
import re

if __name__ == "__main__":
	for line in sys.stdin:
		line = line.lower()
		line = re.sub(r'[^\w\s]|[0-9]+','',line)		
		file_name = os.getenv('map_input_file')
		fname = file_name.rsplit('/', 1)[1]
		words = line.split()
		for w in words:
			sys.stdout.write("{0}\t{1}:{2}\n".format(w,fname,1))
