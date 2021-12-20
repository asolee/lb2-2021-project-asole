import numpy as np
import sys
import math

#perform values
def obtain_values(y_test,y_real):
	#null matrices
	C = [[0,0,0],[0,0,0],[0,0,0]]
	CH = [[0,0],[0,0]]
	CE = [[0,0],[0,0]]
	CC = [[0,0],[0,0]]
	total_len = len(y_real)
	n = 0
	list_test = [1,2,3]
	list_real = [1,2,3]
	#fill the C matrix
	for S in y_real:
		for elSS in list_real:
			for elGOR in list_test:
				if y_real[n] == elSS and y_test[n] == elGOR:
					C[list_real.index(elSS)][list_test.index(elGOR)] = C[list_real.index(elSS)][list_test.index(elGOR)] +1
		n += 1
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


test = (sys.argv[1])
real = (sys.argv[2])

y_test = np.loadtxt(test, dtype=int)
y_real = np.loadtxt(real, dtype=int)

y_test = y_test.tolist()
y_real = y_real.tolist()


obtain_values(y_test,y_real)
