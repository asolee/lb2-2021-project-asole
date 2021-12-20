import os

total_len = 0
total_identity = 0
ID = open("ID_list.txt","r")
for i in ID:
	i = i[:-1]
	dssp = open("GOR_train/"+i+".dssp","r")
	next(dssp)
	for j in dssp:
		j = j[:-1]
	gor = open("GOR_train/"+i+".gor","r")
	next(gor)
	for k in gor:
		k = k
	dssp1 = []
	gor1 = []
	for el in j:
		dssp1.append(el)
	for el in k:
		gor1.append(el)
	print(j)
	print(k)
	print("-----------------------------")
	total_len = total_len + len(gor1)

	for aa in range(0,len(gor1)-1):
		if dssp1[aa]=="-" and gor1[aa]=="C":
			total_identity += 1
		if dssp1[aa]=="H" and gor1[aa]=="H":
			total_identity += 1
		if dssp1[aa]=="E" and gor1[aa]=="E":
			total_identity += 1

print(total_identity/total_len)
