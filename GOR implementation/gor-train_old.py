#modules
import os
import sys
import numpy as np


#list for build null GOR matrix
aa = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
###
dict_aa = {0:'A',1:'R',2:'N',3:'D',4:'C',5:'Q',6:'E',7:'G',8:'H',9:'I',10:'L',11:'K',12:'M',13:'F',14:'P',15:'S',16:'T',17:'W',18:'Y',19:'V'}
window = ['//','-8|H','-7|H','-6|H','-5|H','-4|H','-3|H','-2|H','-1|H','0|H','+1|H','+2|H','+3|H','+4|H','+5|H','+6|H','+7|H','+8|H','-8|E','-7|E','-6|E','-5|E','-4|E','-3|E','-2|E','-1|E','0|E','+1|E','+2|E','+3|E','+4|E','+5|E','+6|E','+7|E','+8|E','-8|-','-7|-','-6|-','-5|-','-4|-','-3|-','-2|-','-1|-','0|-','+1|-','+2|-','+3|-','+4|-','+5|-','+6|-','+7|-','+8|-','-8','-7','-6','-5','-4','-3','-2','-1','0','+1','+2','+3','+4','+5','+6','+7','+8']
dict_window = {0:'//',1:'-8|H',2: '-7|H',3: '-6|H',4: '-5|H',5: '-4|H',6: '-3|H',7: '-2|H',8: '-1|H',9: '0|H',10: '1|H',11: '2|H',12: '3|H',13: '4|H',14: '5|H',15: '6|H',16: '7|H',17: '8|H',18: '-8|E',19: '-7|E',20: '-6|E',21: '-5|E',22: '-4|E',23: '-3|E',24: '-2|E',25: '-1|E',26: '0|E',27: '1|E', 28:'2|E',29: '3|E',30: '4|E',31: '5|E',32: '6|E',33: '7|E',34: '8|E',35: '-8|-',36: '-7|-',37: '-6|-',38: '-5|-',39: '-4|-',40: '-3|-',41: '-2|-',42: '-1|-',43: '0|-',44: '1|-',45: '2|-',46: '3|-',47: '4|-',48: '5|-',49: '6|-',50: '7|-',51: '8|-',52: '-8',53: '-7',54: '-6',55: '-5',56: '-4',57: '-3',58: '-2',59: '-1',60: '0',61: '1',62: '2',63: '3',64: '4',65: '5',66: '6',67: '7',68: '8'}
Structures = ['H','E','-']
dict_Structures = {0:'H',1:'E',2:'-'}
frequency = ['//','F']
dict_frequency = {0:'//',1:'F'}

#obtain a array and sequence from the profile
def obtain_profile(ID,dir):
	sequence = []
####
	ID_matrix = np.zeros((2,20))
	profile=open(dir+'/'+ID+".matrix")
	next(profile)
	for line in profile:
		head = line.split()
		list = line.split()[2:-2]
###
		if len(list) == 20:
			ID_matrix = np.vstack([ID_matrix,[list]])
			sequence.append(head[1])
	ID_matrix = np.delete(ID_matrix,0,0)
	ID_matrix = np.delete(ID_matrix,0,0)
	return ID_matrix,sequence

#obtain SS
def obtain_SS(ID,dir):
	SS = ""
	structure=open(dir+'/'+ID+".dssp")
	next(structure)
	for line in structure:
		SS = line
	return SS

#contruct the go_train_matrix
def gor_train(ID,dir,w_range):
	w_range = int(w_range)
	#half window size for iteration
	if w_range % 2 == 0:
		print("please insert an odd number")
		sys.exit()
###//
	d = int((float(w_range)/2)-0.5)
	#define indeces
	aa = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
	dict_aa = {0:'A',1:'R',2:'N',3:'D',4:'C',5:'Q',6:'E',7:'G',8:'H',9:'I',10:'L',11:'K',12:'M',13:'F',14:'P',15:'S',16:'T',17:'W',18:'Y',19:'V'}
	conf_list = ["H","E","-",""]
	initial_position = 0
	window = []
	window.append("//")
	for i in conf_list:
		for j in range(int(initial_position-d),int(initial_position+d+1)):
			if i == "":
				window.append(str(j))
				continue
			window.append(str(j)+"|"+str(i))
	dict_window = {}
	for i in range(0,len(window)):
		dict_window[int(i)] = window[i]
	#null matrix creation
	GOR_matrix = np.zeros(((w_range*4),20))
	GOR_matrix = np.vstack([aa,GOR_matrix])
	GOR_matrix = np.c_[GOR_matrix,window]
	GOR_S = np.zeros(3)
	GOR_S = np.vstack([Structures,GOR_S])
	GOR_S = np.c_[GOR_S,frequency]
#	print(GOR_matrix)
	#iterate for any ID
	ID = open(ID,"r")
	total_len = 0
#	number_ID = 0
	for i in ID:
###
		i = i[:-1]
		#obtain the profile and sequence of i
		profile,sequence = obtain_profile(i,dir)
		#obtain SS
		SS = obtain_SS(i,dir)
		#important features of profile shape
		num_rows, num_cols = profile.shape
		#take count of windows
###
		pos = 0
		count_ss = 0
		count_line = 0
		length = len(SS)
		total_len = total_len + length
		for line in profile:
			#take count of position inside the window
			iteration = -d
			for w in range(pos-d,pos+d+1):

				if w >= 0 and w < num_rows:
#					print(pos-d)
#					print(pos+d)
#					print(w)
#					print(sequence[w])
#					print(SS[w])
#					print(iteration)
#					print(profile[w])
					lista = profile[w]
#					print(lista)

					#iterate inside list and find aa
					count_aa = 0
					count_ss = count_ss + w
					count_ss += 1
					for el in lista:
						#iterazion
						el = float(el)

						#n of the column in the GOR matrix
						c_key = count_aa

						#n of row in the GOR matrix
						pointer = str(iteration)+"|"+SS[count_ss-1]
						keys = [k for k, v in dict_window.items() if v == pointer]

						#n of row in only window GOR matrix
						pointer_2 = str(iteration)
						keys_2 = [k for k, v in dict_window.items() if v == pointer_2]

						#add values to GOR
						GOR_matrix[keys[0],c_key] = float(GOR_matrix[keys[0],c_key]) + el
						GOR_matrix[keys_2[0],c_key] = float(GOR_matrix[keys_2[0],c_key]) + el

						count_aa += 1
						if count_aa == 19:
							count_aa == 0

				#fill the submatrix related to structures
				if count_line < len(SS)-1:
					pointer_3 = str(SS[count_line])
					keys_3 = [k for k, v in dict_Structures.items() if v == pointer_3]
					GOR_S[1,keys_3[0]] = float(GOR_S[1,keys_3[0]]) + 1

				count_ss = 0
				count_line += 1
				iteration += 1
				if w == pos+d+1:
					iteration = -d
#			print("___________________")
			pos = pos + 1

#		print("done"+str(number_ID))
#		number_ID += 1

	#obtain values to normalize all rows
	rows,cols = GOR_matrix.shape
	RK = GOR_matrix[rows-(d*2)-1:]
	RK = np.delete(RK,-1,axis=1)
	RK_sums = []
	for i in RK:
		RK_row = 0
		for j in i:
			RK_row = RK_row + float(j)
		RK_sums.append(RK_row)

	#normailze GOR matrix
?	n = 1
	for j in range(0,((d*2)+1)):
		for i in range(n,rows,((d*2)+1)):
			print(i)
			cl = 0
			for q in GOR_matrix[i,:-1]:
				GOR_matrix[i,cl] = float(GOR_matrix[i,cl])/RK_sums[n-1]
				cl += 1
		n += 1

	#normalize GOR matrix with N
#	for i in range(1,rows):
#		for j in range(0,cols-1):
#			print(GOR_matrix[i,j])

	#normalize GOR submatrix
	for i in range(1,2):
		for j in range(0,3):
			try:
				GOR_S[i,j] = float(GOR_S[i,j])/total_len
			except ValueError:
				pass

	#print matrices
#	output = open(output,'w')
	np.set_printoptions(threshold=np.inf)
#	output.write(GOR_matrix)
#	output.write("#######")
#	output.write(GOR_S)
	GOR_matrix = GOR_matrix.tolist()
	GOR_S = GOR_S.tolist()
	print(GOR_matrix)
	print("#")
	print(GOR_S)

if __name__ == "__main__":
	input_ID = (sys.argv[1])
	input_directory = (sys.argv[2])
	window_range = (sys.argv[3])

gor_train(input_ID,input_directory,window_range)

