#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  separapals.py
#  
#  Copyright 2015 Icaro Duarte gavazza Lima <icarodgl@gmail.com>

def separaPals(paramtxt):
	strbuffer = ""
	lst = []
	
	for elem in paramtxt:
		if (elem == "-" or elem == "'") or elem.isalnum():
			strbuffer += elem
		else:
			if strbuffer != "":
				lst.append(strbuffer)
				strbuffer = ""			
			#if
		#else
	#for
	if len(strbuffer) > 0:
		lst.append(strbuffer)
		
	return lst


def main():
	
	return 0

if __name__ == '__main__':
	main()

