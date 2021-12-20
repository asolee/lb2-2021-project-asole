import sys
import numpy as np
import math
import os
import ast

def full_matrix(file):
	matrix = open(file,"r")
	m = []
	s = []
	for line in matrix:
		line = line.rstrip()
		if line != "#":
			matr = ast.literal_eval(line)
			m.append(matr)
	m0 = m[0]
	m0 = np.asarray(m0)
	m0 = m0.astype(np.float64)
	m1 = m[1]
	m1 = np.asarray(m1)
	m1 = m1.astype(np.float64)
	m2 = m[2]
	m2 = np.asarray(m2)
	m2 = m2.astype(np.float64)
	m3 = m[3]
	m3 = np.asarray(m3)
	m3 = m3.astype(np.float64)
	m4 = m[4]
	m4 = np.asarray(m4)
	m4 = m4.astype(np.float64)
	m_tot = m0 + m1 + m2 + m3 + m4
	m_tot = m_tot/5
	print(m_tot)
	m_group = [m0,m1,m2,m3,m4]
	stdev_m = np.zeros((5,3))
	stdev_m = np.std(m0,m1,m2,m3,m4)
	print(stdev_m)



if __name__ == "__main__":
	matrix = (sys.argv[1])

full_matrix(matrix)
