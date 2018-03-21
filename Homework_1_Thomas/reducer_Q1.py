#!/usr/bin/env python

import sys

if __name__=="__main__":
	curr_word = None
	word=None
	file_names=[]

	for line in sys.stdin:
		word,fname=line.split("\t")
		fname=fname.strip()

		if word==curr_word:
			if fname not in file_names:
				file_names.append(fname)
		else:
			if curr_word is not None:
				sys.stdout.write("{0}\t{1}\n".format(curr_word,file_names))
			
			curr_word=word
			file_names=[]
			file_names.append(fname)

	if curr_word:
		sys.stdout.write("{0}\t{1}\n".format(curr_word,file_names))
