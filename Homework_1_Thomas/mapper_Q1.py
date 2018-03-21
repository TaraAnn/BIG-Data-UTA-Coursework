#!/usr/bin/env python

import sys
import os
import re

if __name__ == "__main__":
	for line in sys.stdin:
		line = line.lower()
		line = re.sub(r'[^\w\s]|[0-9]+','',line)
		filename = os.getenv('map_input_file')
		file_name = filename.rsplit('/', 1)[1]
        	words = line.split()
		for word in words:
			sys.stdout.write("{0}\t{1}\n".format(word, file_name))
