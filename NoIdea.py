
z = raw_input()
n = raw_input()
l1 = n.split()
l2 = list(map(int,l1))
print(l2)
m1 = raw_input()
l3 = m1.split()
l4 = list(map(int,l3))
print(l4)
m2 = raw_input()
l5 = m2.split()
l6 = list(map(int,l5))
print(l6)

happyness=0
for i in l4:
    if i in l2:
        happyness = happyness + 1
for i in l6:
    if i in l2:
        happyness = happyness -1
print(happyness)

