#modules
import os
import sys
import numpy as np
import math

#obtain SS
def obtain_SS(ID,dir):
	SS = ""
	#open the dssp file
	structure=open(dir+'/'+ID+".dssp")
	next(structure)
	#string of SS
	for line in structure:
		line = line.rstrip()
		SS = line
	return SS

#obtain a array and sequence from the profile
def obtain_profile(ID,dir):
	sequence = ""
	#open the profile file
	profile=open(dir+'/'+ID+".matrix")
	next(profile)
	ID_matrix=[]
	#create sequence string and frequency table
	for line in profile:
		aa = line.split()
		frequency = line.split()[2:-2]
		#avoid [] in last position
		if len(frequency) == 20:
			aa = aa[1]
			ID_matrix.append(frequency)
			sequence = sequence+aa
	ID_matrix = np.asarray(ID_matrix)
	#convert all elements in float numbers
	ID_matrix = ID_matrix.astype(np.float64)
	return ID_matrix,sequence

#obtain the gor matrix and info for normalization
def SVM_list(ID,dir,w_range):
	#total len for normalization
	total_len = 0
	#check if the size of the window is an odd number
	if w_range %2 == 0:
		print("please insert an odd number")
		sys.exit()
	#define important parameters of the window
	d = w_range//2
	#create a null row to padd
	padd_m = np.zeros(20)
	#iterate for every ID in the list of IDs
	ID=open(ID,"r")
	total_svm_x = []
	total_X = open(dir+"/TOTAL.SVMX","w")
	for id in ID:
		id = id.rstrip()
		#obtain profile and sequence
		try:
			profile,sequence = obtain_profile(id,dir)
		except (FileNotFoundError,UnboundLocalError) as ex:
			continue
		#obtain SS
		SS = obtain_SS(id,dir)
		#important features on profile shape
		num_rows, num_cols = profile.shape
		#iterate on each row of profile
		c_pos = 0
		total_len = total_len + len(SS)
		#initailize the file for svm
		for line in profile:
			#define the structure of central position
			string = SS[c_pos]
			#define a matrix that contain the window
			window_m = []
			for w in range(c_pos-d,c_pos+d+1):
				#set condition to avoid negative and oversize iterations
				if w >= 0 and w < num_rows:
					lista = profile[w]
					window_m.append(lista)
			#numpy format
			window_m = np.asarray(window_m)
			w_rows, w_cols = window_m.shape
			#padd the matrices
			if c_pos < d:
				for n in range(w_rows,(d*2)+1):
					window_m = np.vstack([padd_m, window_m])
			if c_pos > (num_rows-d-1):
				for n in range(w_rows,(d*2)+1):
					window_m = np.vstack([window_m, padd_m])
			window_m = window_m.astype(np.float64)
			window_m = window_m.tolist()
			all_window = []
			for list in window_m:
				for i in list:
					i = float(i)
					all_window.append(i)
			total_svm_x.append(all_window)
			c_pos += 1
	c = 0
	for i in total_svm_x:
		c += 1
	print(c)
	total_svm_x = np.asarray(total_svm_x)
	total_svm_x = total_svm_x.astype(np.float64)
	print(total_svm_x.shape)
	np.savetxt((sys.argv[4]), total_svm_x, fmt='%1.2f')

if __name__ == "__main__":
	input_ID = (sys.argv[1])
	input_dir = (sys.argv[2])
	window_range = (int(sys.argv[3]))
	output = (sys.argv[4])
SVM_list(input_ID,input_dir,window_range)
