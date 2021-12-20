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

#normalize matrices
def normalize_matrix(info,margin):
	info = info.tolist()
	margin = margin.tolist()
	r = 0
	for row in info:
		c = 0
		for value in row:
			N = sum(margin[r])
			info[r][c] = info[r][c]/N
			c += 1
		r += 1
	info = np.asarray(info)
	return info

def log_matrix(info,margin,S):
	info = info.tolist()
	margin = margin.tolist()
	r = 0
	for row in info:
		c = 0
		for value in row:
			info[r][c] = info[r][c]/(margin[r][c]*S)
			try:
				info[r][c] = math.log(float(info[r][c]),10)
			except ValueError as ex:
				info[r][c] = info[r][c]
			c += 1
		r += 1
	info = np.asarray(info)
	return info


#obtain the gor matrix and info for normalization
def gor_train(ID,dir,w_range):
	#total len for normalization
	total_len = 0
	#check if the size of the window is an odd number
	if w_range %2 == 0:
		print("please insert an odd number")
		sys.exit()
	#define important parameters of the window
	d = w_range//2
	#initialize the null matrix in base of window size.
	H_info = np.zeros((w_range,20))
	E_info = np.zeros((w_range,20))
	C_info = np.zeros((w_range,20))
	M_info = np.zeros((w_range,20))
	GOR_S = np.zeros(3)
	#create a null row to padd
	padd_m = np.zeros(20)
	#iterate for every ID in the list of IDs
	ID=open(ID,"r")
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
		for line in profile:
			#define the structure of central position
			str = SS[c_pos]
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
			#fill the correct infomatrix,margin and structure
			if str == "H":
				H_info = H_info + window_m
				M_info = M_info + window_m
				GOR_S[0] = GOR_S[0] + 1
			if str 	== "E":
				E_info = E_info + window_m
				M_info = M_info + window_m
				GOR_S[1] = GOR_S[1] + 1
			if str == "-":
				C_info = C_info + window_m
				M_info = M_info + window_m
				GOR_S[2] = GOR_S[2] + 1
			c_pos += 1
	#normalize GOR_S
	GOR_S = GOR_S/total_len

	#normalize matrices
	H_info = normalize_matrix(H_info,M_info)
	E_info = normalize_matrix(E_info,M_info)
	C_info = normalize_matrix(C_info,M_info)
	M_info = normalize_matrix(M_info,M_info)

	#log matrices
	H_info = log_matrix(H_info,M_info,GOR_S[0])
	E_info = log_matrix(E_info,M_info,GOR_S[1])
	C_info = log_matrix(C_info,M_info,GOR_S[2])

	#save in a better way
	H_info = H_info.tolist()
	E_info = E_info.tolist()
	C_info = C_info.tolist()
	M_info = M_info.tolist()
	GOR_S = GOR_S.tolist()
	print(H_info)
	print("#")
	print(E_info)
	print("#")
	print(C_info)
	print("#")
	print(M_info)
	print("#")
	print(GOR_S)



if __name__ == "__main__":
	input_ID = (sys.argv[1])
	input_dir = (sys.argv[2])
	window_range = (int(sys.argv[3]))

gor_train(input_ID,input_dir,window_range)
