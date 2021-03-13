import re

for i in range(101,901):
	filename ='%i.vcf'%(i)

	f = open(filename)
	lines = f.readlines()
	f.close()
	f = open(filename, 'w')

	for line in lines:
		if line[0:7]=="VERSION":
			f.write("VERSION:2.1\n")
		elif re.search("EMAIL", line):
			f.write(line[6:])
		elif line[0:4] == "item":
			f.write("")
		elif line[0:4]=="NOTE":
			f.write("")
		elif line[0:6]=="PHOTO:":
			f.write("")
		elif line[0:1]==" ":
			f.write("")
		elif line[0:11]=="CATEGORIES:":
			f.write("")
		else:
			f.write(line)
	f.close()
