#!/usr/bin/env python
import sys

if __name__=="__main__":
	curr_word = None
	word=None	
	total=0
	output_dict={}

	for line in sys.stdin:
		word,temp=line.split("\t")
		fname,count=temp.split(":")
		count=int(count)
		fname=fname.strip()

		if word==curr_word:
			total+=count
			output_dict[fname]=total
		else:
			if curr_word is not None:
				sys.stdout.write("{0}\t{1}\n".format(curr_word,output_dict))
			curr_word=word
			total=count
			output_dict={}
			output_dict[fname]=total
			
	if curr_word:
		sys.stdout.write("{0}\t{1}\n".format(curr_word,output_dict))
