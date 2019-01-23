#SLICES DEMO

print("Slices Demo"*3)

colours = ["Mujtaba","Asif","Imad","Rizwan","Sarfaraz"]
print(len(colours))
print(colours[0:len(colours)])
print(colours[0:5])
print(colours[0:5:1])
print(colours[0:5:2])
print(colours[0:5:-1])
print(colours[0::-1])
print(colours[5::-1])
print(colours[2::-1])
print(colours[:5:-1])
print(colours[:3:-1])
print(colours[0:5:-1])
print(colours[1:4])

trial = [1,2,3,4,5,6]
print(trial)
print(trial[0:5])
print(trial[6::-1])
print(trial[:1:-1])
print(trial[6:1:-1])
print(trial[5:2:-1])
print(colours[4][::-1])


#LIST COMPREHENSION
name = "Syed Mujtaba Arfat"

name2 =[char for char in name if char not in "aeiou"]
print("".join(name2))


even = [ num for num in range(1,50) if num%2==0]
print(even)

odd = [num for num in range(1,50) if num%2!=0]
print(odd)

num_list = [num*2 if num%2==0 else num *1 for num in range(1,60)]
print(num_list)



#[[1 2 3] [ 1 2 3 ] [1 2 3 ]]

demo = [[ num for num in range(1,4) ]for val in range(1,5)]

print(demo)

l1=[1,2,3,4,5,6,7,8,9]
output=[]
i=0;
while i<len(l1):
	output.append(l1[i:i+3])
	i=i+3;
print(output)
l2=[num*3 for num in l1]
print(l2)
out=[]
i=0
while(i<len(l2)):
	out.append(l2[i:i+1])
	i=i+3
print(out)
[["X" if num%2!=0 else "O" for num in range(1,4)] for val in range(1,4)]

answer =[[x for x in range(0,10)] for val in range(1,9)]
print(answer)




#DICTIONARIES

artist={
	
	"first":"Niel",
	"last":"Young"
}

full_name =artist['first']+" "+artist['last']
print(full_name)
instructor = {"name":"Arfat","age":21,"num":32}

for key in instructor.keys():
	print(key)

for val in instructor.values():
	print(val)

for key,val in instructor.items():
	print("key:{} val:{}".format(key,val))


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!
total_donations=0
for val in donations.values():
    total_donations=total_donations+val

total_donations = sum(donations.values())



# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list={}
stock_list.update(inventory)

# add the value 18 to stock_list under the key "cookie"
stock_list.update(cookie=18)


# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")

print(stock_list)


#Spotify playlist


playlist ={"title":"Mylist",
			"Created_by":"Arfat",
			"Songs":[{'title':'song1','artist':['blue'],'duration':2.5},{'title':'song1','artist':['blue'],'duration':3.5}]}


for song in playlist['Songs']:
	print(song['duration'])



list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can 
answer ={list1[i]:list2[i] for i in range(0,3)}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0]:person[i][1] for i in range(0,3)} 
print(answer)

sample ="aeiou"
answer = {i:0 for i in "aeiou"}
print(answer)
answer = {x:chr(x) for x in range(65,91)}
print(answer)

list4 = ["january","feb","march"]
print(list4)
tup=("january","feb","march")
print(tup)