#! /usr/bin/python3

import configparser

def main():
	
	cfg = configparser.ConfigParser()
	cfg.read( "configparser_demo.txt")
	common_sect = cfg["Common"]
	lang_sect = cfg["Lang"]
	for k, v in enumerate( common_sect): 
		print( f"{k}:{v}")
	for k, v in enumerate( lang_sect ): 
		print( f"{k}:{v}")
main()
