import sys

def clean(file,file2):
	H = ["H","G","I"]
	E = ["B","E"]
	C = ["T","S","C"]
	input = open(file,"r")
	next(input)
	for line in input:
		seq = ""
		print(line)
		for i in line:
			if i in H:
				seq = seq+"H"
				continue
			if i in E:
				seq = seq+"E"
				continue
			if i in C:
				seq = seq+"C"
				continue
			seq = seq+"C"
	print(seq)
	output = open(file2,"w")
	output.write(">"+sys.argv[1][:-10]+"\n")
	output.write(seq)
	input.close()
	output.close()

if __name__ == "__main__":
	file = (sys.argv[1])
	file2 = (sys.argv[2])

clean(file,file2)
