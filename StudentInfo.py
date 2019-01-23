
studentinfo = raw_input()

lis = studentinfo.split()
print(lis)
i = 0
finalinfo = {}
while i<len(lis):
	finalinfo[lis[i]]=int(lis[i+1],10)
	i=i+2
print(finalinfo)


while(1):
	name = raw_input("Enter name\n")
	value = raw_input("roll no")
	lis.append(name)
	lis.append(value)
	print(lis)



