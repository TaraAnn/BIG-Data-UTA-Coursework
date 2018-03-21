#!/usr/bin/env python
import sys

if __name__=="__main__":
	current_author=None	
	total=0
	count=0
	output_dict={}

	for line in sys.stdin:
		auth,temp=line.split("\t")
		word,count=temp.split(":")
		count=int(count)
		auth=auth.strip()
		word=word.strip()

		if auth==current_author:
			total+=count
			output_dict[word]=total
		else:
			if current_author is not None:
				sys.stdout.write("{0}\t{1}\n".format(current_author,output_dict))
			current_author=auth
			total=count
			output_dict={}
			output_dict[word]=total
			
	if current_author:
		sys.stdout.write("{0}\t{1}\n".format(current_author,output_dict))
