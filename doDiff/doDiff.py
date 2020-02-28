#! /usr/bin/python3

import difflib
import os 

def main():
	file1 = 'a.txt'
	file2 = "b.txt"
	with open(file1, "r", encoding="utf-8") as fp: content1 = fp.readlines()
	with open(file2, "r", encoding="utf-8") as fp: content2 = fp.readlines()

	differ = difflib.HtmlDiff( tabsize=2, wrapcolumn=80 )
	res = differ.make_file( content1, content2, fromdesc= file1, todesc= file2 , context=True , numlines= 20 )

	diffFile = "diff_output.html"
	with open( diffFile, "w", encoding="utf-8") as fp:
		fp.write(res) 
	print( "check file %s" % ( diffFile ))
main()
