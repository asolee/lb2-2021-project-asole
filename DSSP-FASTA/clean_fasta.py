import sys

def clean(file,file2):
	list = ["H","B","E","G","I","T","S"]
	input = open(file,"r")
	output = open(file2,"w")
	next(input)
	for line in input:
		seq = ""
		print(line)
		for i in line:
			if i not in list:
				seq = seq+"C"
				continue
			seq = seq+i
	print(seq)
	output.write(">"+sys.argv[1][:-6]+".dssp\n")
	output.write(seq)
	input.close()
	output.close()

if __name__ == "__main__":
	file = (sys.argv[1])
	file2 = (sys.argv[2])

clean(file,file2)
