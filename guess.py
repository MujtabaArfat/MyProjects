from random import randint

ran = randint(1,10)

x = input("Enter the number")
while(int(x)!=ran):
	if(int(x)<ran):
		print("Too low")
		x = input("Enter new guess")
	elif(int(x)>ran):
		print("too high")
		x = input("Enter new guess")
print("{} yes u guessed it".format(int(x)))
friend = ["Undertaker","John","Batista"]

print(friend[0])
print(friend[2])

items =["Asif","Imad","Rizwan","Sarfaraz","Talha"]

for num in range(len(items)):
	if items[num]=="Sarfaraz":
		print("found at {} and is {}".format(num,items[num]))

if "Mujtaba" in items:
	print("True")
else :
	print("False")

test = ["Syed","Mujtaba","Arfat"]
result = " "
for x in test:
	x=x.upper()
	result +=x
print(result)
