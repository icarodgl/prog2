#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  autopush.py
#  
#  Copyright 2015 Icaro <icaro@icaro-X550CA>
import sys
import os
def main():

	text = "upado por autopush"
	os.system("git add .")
	#text = input("mensagem: ")
	os.system("git commit -m "+ text)
	os.system("git push")	
	return 0
#	if len(sys.argv) == 2:
#		text = sys.argv[1]
#		os.system("git add .")
		#text = input("mensagem: ")
#		os.system("git commit -m "+ text)
#		os.system("git push")
#	else:
#		print("argumento MENSAGEM não foi digitado")


if __name__ == '__main__':
	main()

