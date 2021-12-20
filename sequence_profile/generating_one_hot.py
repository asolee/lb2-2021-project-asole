import sys

def split(sequence):
        return [char for char in sequence]

def matrix_isolation(file,file2):
        null_matrix = 0
        all_matrix = []
        aminoacids = [' ',' ','A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
        input = open(file,"r")
        next(input)
        for line in input:
                head = []
                print(split(line))
                sequence = split(line)
                n = 1
                for S in sequence:
                        head = [n,S]
                        n += 1
                        values = []
                        for i in range(20):
                                values.append(0)
                        true_aminoacids = aminoacids[2:]
                        for i in true_aminoacids:
                                if i == S:
                                        position = true_aminoacids.index(i)
                                        values[position] = 1
                        print(values)
                        matrix = head + values
                        print(matrix)
                        all_matrix.append(matrix)
        print(all_matrix)
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

