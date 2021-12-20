import sys

def matrix_isolation(file,file2):
	null_matrix = 0
	all_matrix = []
	aminoacids = [' ',' ','A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
	input = open(file,"r")
	for i in range(3):
		next(input)
	for line in input:
		head = []
		aa = line.split()
		if len(aa) > 5:
			head = [aa[0],aa[1]]
			values = aa[22:]
			values_100 = []
			for v in values:
				v = float(v)/100
				values_100.append(v)
				n = 0
				for el in values_100:
					if el == 0.0:
						n += 1
				if n == 22:
					null_matrix += 1
			matrix = head + values_100
			print(matrix)
			all_matrix.append(matrix)
	l = all_matrix[-1][0]
	print(l)
	print(null_matrix)
	if int(l) != int(null_matrix):
		output = open(file2,"w")
		for i in aminoacids:
			output.write(i+"\t")
		output.write("\n")
		for f in all_matrix:
			for j in f:
				output.write(str(j)+"\t")
			output.write("\n")
		output.write("\n")



file = (sys.argv[1])
file2 = (sys.argv[2])
matrix_isolation(file,file2)
