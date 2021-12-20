

import sys
import numpy as np
import ast
import math
import os

def read_GOR_matrix(GOR_file):
	#open the file that contain the two GOR matrices
	GOR_file = open(GOR_file,"r")
	#retrieve the two matrices
	all_matrix = []
	for line in GOR_file:
		if line != "#\n":
			line = ast.literal_eval(line[:-1])
			all_matrix.append(line)
	#divide the twp matrices
	H_info = np.asarray(all_matrix[0])
	E_info = np.asarray(all_matrix[1])
	C_info = np.asarray(all_matrix[2])
	R_matrix = np.asarray(all_matrix[3])
	S_matrix = np.asarray(all_matrix[4])
	return(H_info,E_info,C_info,R_matrix,S_matrix)

#obtain a array and sequence from the profile
def obtain_profile(ID,dir):
	sequence = []
	ID_matrix = []
	profile=open(dir+'/'+ID+".matrix")
	next(profile)
	for line in profile:
#		head = line.split()
		list = line.split()[2:-2]
		if len(list) == 20:
			ID_matrix.append(list)
#			sequence.append(head[1])
	ID_matrix = np.asarray(ID_matrix)
	return ID_matrix

def find_SS(GOR_file,ID_list,dir):
	H_info,E_info,C_info,R_matrix,S_matrix = read_GOR_matrix(GOR_file)
#	print(H_info,E_info,C_info)
	IDs = open(ID_list,'r')
	d = len(H_info)//2
#	print(d)
	n_p = 1
	for ID in IDs:
		ID = ID.rstrip()
		#open the file where we write the SS
		output = open(dir+"/"+ID+".gor","w")
		#write the fasta format like part
		out_head = ">"+ID+"\n"
		output.write(out_head)
		#initalize SS
		SS = ''
		#obtain the profile for each ID
		try:
			profile = obtain_profile(ID,dir)
		except (FileNotFoundError,UnboundLocalError) as ex:
			continue
		#shape of the sequence matrix
		num_rows,numcols=profile.shape
		#take count of windows
		pos = 0
		#ierate for every position in the sequence profile
		for line in profile:
			window_matrix = []
			#define the window
			for w in range(pos-d,pos+d+1):
#				print(w)
				if w >= 0 and w < num_rows:
					lista = profile[w]
					window_matrix.append(lista)
			#obtain a matrix for each window
			window_matrix =np.asarray(window_matrix)
			n_rows, n_cols = window_matrix.shape
			#row to fill the incomplete matrices
			fill_row = np.zeros(20)

			#check start incomplete windows and correct
			if pos < d:
				for n in range(n_rows,(d*2)+1):
					window_matrix = np.vstack([fill_row, window_matrix])

			#check the end incomplete windiws and correct
			if pos > (num_rows-d):
				for n in range(n_rows,(d*2)+1):
					window_matrix = np.vstack([window_matrix, fill_row])
#			print(window_matrix)
			#obtain the values by multiplyng with info matrices
			values_H = []
			values_E = []
			values_C = []
			r = 0
			#perform by iteration the product of each position
			for rows in window_matrix:
				c = 0
				for value in rows:
					values_H.append((float(value)*float(H_info[r,c])))
					values_E.append((float(value)*float(E_info[r,c])))
					values_C.append((float(value)*float(C_info[r,c])))
					c += 1
				r += 1
			#sum the result of all the position to obtain the three final scores
			total_H = sum(values_H)
			total_E = sum(values_E)
			total_C = sum(values_C)
			#compute wich conformation need to add in the sequence
			letter = ''
			if total_H > max(total_E,total_C):
				letter = 'H'
			if total_E > max(total_H,total_C):
				letter = 'E'
			if total_C > max(total_H,total_E):
				letter = 'C'

			#add the letter at the SS
			SS = SS+letter

			#pass to the next position
			pos = pos + 1
		print(n_p)
		n_p += 1
		output.write(SS)
		output.close()
#		print('done')















if __name__ == "__main__":
        input_matrix = (sys.argv[1])
        ID_list = (sys.argv[2])
        directory = (sys.argv[3])

#evaluate_info_matrices(input_matrix)
find_SS(input_matrix,ID_list,directory)
