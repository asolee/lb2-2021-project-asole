# -*- coding: utf-8 -*-
import sys
import numpy as np
 
def convert(ID_lista,Directory):
	#open the ID list
	ID_list = open(ID_lista,"r")
	total_y = []
	#iterate for every ID in the list
	for ID in ID_list:
		ID = ID.rstrip()
		#initialize a new list
		SVM_list = []
		#open the dssp_file that correspond to the ID
		try:
			dssp_file = open(sys.argv[2]+"/"+ID+".dssp","r")		
		except (FileNotFoundError,UnboundLocalError) as ex:
			continue
		next(dssp_file)
		#iterate for every dssp sequence
		for dssp in dssp_file:
			dssp = dssp[:-1]
			print(dssp)
			for el in dssp:
				if el == "H":
					SVM_list.append(1)
				if el == "E":
					SVM_list.append(2)
				if el == "-":
					SVM_list.append(3)
		for el in SVM_list:
			total_y.append(el)
	c = 0
	for i in total_y:
		c += 1
	print(c)
	total_y = np.asarray(total_y)
	total_y = total_y.astype(np.float64)
	print(total_y.shape)
	np.savetxt('TOTAL.SVMY', total_y, fmt='%d')

ID_lista = (sys.argv[1])
Directory = (sys.argv[2])

convert(ID_lista,Directory)
