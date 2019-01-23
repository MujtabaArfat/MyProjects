from random import randint
num = randint(1,20)
num1 = input()

while True:
	if num1<num:
		print("TOO LOW")
		num1=input()
	elif num1>num:
		print("TOO high")
		num1= input()
	elif num1==num:
		print("Equal")
		num = randint(1,20)
		num1 = input("Enter new guess")
