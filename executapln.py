#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  executapln.py
#  
#  Copyright 2015 Icaro <icaro@icaro-X550CA>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
from libpln import *
def main():
	ajuda=["ajuda","help","-h"]
	ng = ["ngrama","N_grama","n_grama"]
	if sys.argv[1] in ajuda:
		print("executapln.py + nome_da_função + argumento")
		print("ngrama argtxt argint")
	if len(sys.argv) == 4:
		if sys.argv[1] in ng:
			
			fun = n_grama(sys.argv[2],int(sys.argv[3]))
			print(fun)
		if sys.argv[1] == "corrente":
			fun = corrente(sys.argv[2],int(sys.argv[3]))
			print(fun)
	return 0

if __name__ == '__main__':
	main()

