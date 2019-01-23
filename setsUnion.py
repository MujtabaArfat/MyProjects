# Enter your code here. Read input from STDIN. Print output to STD
lim1 = raw_input()
a = raw_input()
lis = a.split()
newlis = list(map(int, lis))
lim2 = raw_input()
b= raw_input()
lis2 = b.split()
newlis2 = list(map(int,lis2))
s1=set(newlis)
s2=set(newlis2)
s3 =(s1.difference(s2))
s4=(s2.difference(s1))
s5=s3.union(s4)
sorted(s5)

for i in s5:
    print i

