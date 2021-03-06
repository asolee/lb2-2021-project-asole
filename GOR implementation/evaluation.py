import sys
import numpy as np
import math
import os

#obtain SS
def obtain_SS(ID,dir):
	SS = ""
	structure=open(dir+'/'+ID+".dssp")
	next(structure)
	for line in structure:
		SS = line
	return SS

#obtain gor
def obtain_gor(ID,dir):
	gor = ""
	structure=open(dir+'/'+ID+".gor")
	next(structure)
	for line in structure:
		gor = line
	return gor

#perform values
def obtain_values(ID,dir):
	#null matrices
	C = [[0,0,0],[0,0,0],[0,0,0]]
	CH = [[0,0],[0,0]]
	CE = [[0,0],[0,0]]
	CC = [[0,0],[0,0]]
	#iterate on ID
	ID_list = open(ID,"r")
	total_len = 0
	#obtain ss
	for ID in ID_list:
		ID = ID[:-1]
		print(ID)
		#obtain gor
		try:
			gor = obtain_gor(ID,dir)
		except (FileNotFoundError,UnboundLocalError) as ex:
			continue
		#obtain SS
		try:
			SS = obtain_SS(ID,dir)
		except (FileNotFoundError,UnboundLocalError) as ex:
			continue
		print(gor)
		print("_____")
		print(SS)
		print("____")
		#compute the total len
		total_len = total_len + len(SS)
		n = 0
		listSS = ["H","E","C"]
		listGOR = ["H","E","C"]
		#fill the C matrix
		for S in gor:
			for elSS in listSS:
				for elGOR in listGOR:
					if SS[n] == elSS and gor[n] == elGOR:
						C[listSS.index(elSS)][listGOR.index(elGOR)] = C[listSS.index(elSS)][listGOR.index(elGOR)] +1
			n += 1
	print(total_len)
	#construct the 2H matrix
	CH[0][0] = C[0][0]
	CH[0][1] = C[0][1] + C[0][2]
	CH[1][0] = C[1][0] + C[2][0]
	CH[1][1] = C[1][1] + C[1][2] + C[2][1] + C[2][2]
	CH = np.asarray(CH)
	#construct the 2E matrix
	CE[0][0] = C[1][1]
	CE[0][1] = C[1][0] + C[1][2]
	CE[1][0] = C[0][1] + C[2][1]
	CE[1][1] = C[0][0] + C[0][2] + C[2][0] + C[2][2]
	CE = np.asarray(CE)
	#construct the 2C matrix
	CC[0][0] = C[2][2]
	CC[0][1] = C[2][0] + C[2][1]
	CC[1][0] = C[0][2] + C[1][2]
	CC[1][1] = C[0][0] + C[0][1] + C[1][0] + C[1][1]
	CC = np.asarray(CC)
	#valuate general coefficients
	Q3 = (C[0][0] + C[1][1] + C[2][2])/total_len
	matrices = [CH,CE,CC]
	MCC = []
	SEN = []
	PPV = []
	ACC = []
	for m in matrices:
		mcc = ((m[0][0]*m[1][1])-(m[1][0]*m[0][1]))/math.sqrt((m[0][0]+m[1][0])*(m[0][0]+m[0][1])*(m[1][1]+m[1][0])*(m[1][1]+m[0][1]))
		MCC.append(mcc)
		sen = m[0][0]/(m[0][0]+m[0][1])
		SEN.append(sen)
		ppv = m[0][0]/(m[0][0]+m[1][0])
		PPV.append(ppv)
		acc = (m[0][0]+m[1][1])/(m[0][0]+m[0][1]+m[1][0]+m[1][1])
		ACC.append(acc)
	#print in a better way the matrices
	C = np.asarray(C)
	print("3-class matrix\n")
	print(C)
	print("\n2-class H matrix\n")
	print(CH)
	print("\n2-class E matrix\n")
	print(CE)
	print("\n2-class C matrix\n")
	print(CC)
	print("\nQ3: ",Q3)
	print("MMC: ",MCC[0],MCC[1],MCC[2])
	print("SEN: ",SEN[0],SEN[1],SEN[2])
	print("PPV: ",PPV[0],PPV[1],PPV[2])
	print("ACC: ",ACC[0],ACC[1],ACC[2])
	full_matrix = [[Q3],[MCC[0],MCC[1],MCC[2]],[SEN[0],SEN[1],SEN[2]],[PPV[0],PPV[1],PPV[2]],[ACC[0],ACC[1],ACC[2]]]
	print(full_matrix)


if __name__ == "__main__":
	ID_list = (sys.argv[1])
	directory = (sys.argv[2])

obtain_values(ID_list,directory)
