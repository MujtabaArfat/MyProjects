


def build(l):
	n=1
	a=[]
	b=[]
	i=0


	while(i<len(l)):
		if(l[i]==n):
			a.append(l[i])
			i=i+1
		else:
			b.append(a)
			a=[]
			i=i+1

	return b
print(build([1,1,2,1,2,1,1,3]))

def build(l):
	n=1
	if i>len(l):
		return []
	else:
		return list((list(filter lambda b:b.append(x) if x==1 else b.append(x)))
print(build([1,2,1,3,1,1,2,1]))

