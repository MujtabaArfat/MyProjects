
def fav_colour(first,**kwargs):
	print(first)
	if "arfat" in kwargs:
		print(kwargs['arfat'])
fav_colour("John",arfat="jon",rupert="kane")

def combine_words(word,**kargs):
    if "prefix" in kargs:
        print("{}{}".format(kargs['prefix'],word))
    elif "suffix" in kargs:
        print("{}{}".format(word,kargs['suffix']))
    else:
        print(word)
combine_words("child")
combine_words("child",prefix="man")
combine_words("child",suffix="ish")

 # "The result is 0.7"


def calculate(**kargs):
    if "message" in kargs.keys():
        return kargs['message']+" "+str((kargs['first']+kargs['second']))
    else:
        return "The result is"+str((kargs['first']+kargs['second']))



print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))# "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5))

cube = lambda num:num*num*num
print(cube(2))

def decrement_list(x):
    l = []
    for i in x:
        l.append(i-1)
    return l
print(decrement_list([1,2,3,4]))
def remove_negatives(l):
    return list(filter(lambda n:n>0,l))

print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,4,5]))

print(all([char for char in 'eio' if char in 'aeio']))

def extremes(l):
	x=[]
	x.append(min(x for x in l))
	x.append(max(x for x in l))
	return tuple(x)
print(extremes([1,2,3,4,5]))

l = [10,20,-30]
print(max([ abs(c) for c in l]))
def sum_even(*l):
	x = []
	for i in l:
		print(i)
		if i%2==0:
			x.append(i)
	print(x)
	


	return sum(x)
print(sum_even(1,20,30))

midterms = [80,91,78]
finals =[98,89,53]
students =['dan','ang','kate']

z = list(zip(midterms,finals))
k=[max(c) for c in z]
print(k)
l = zip(students,k)
print(dict(l))

grades=dict(zip(
	students,map(
		lambda pair:max(pair),
		zip(midterms,finals))))
print(grades)

def interleave(s1,s2):
	l = (zip(s1,s2))
	k= ["".join(pair) for pair in l]
	print(k)
	sol=""
	for i in k:
		sol=sol+i
	return sol




print(interleave('hi','ha'))

def triple_and_filter(l):
    z = [c*3 for c in l if c%4==0]
    return z
print(triple_and_filter([1,2,3,4]))

def triple_and_filter(l):
	return [n*3 for n in list(filter(lambda n:n%4==0,l))]
print(triple_and_filter([1,2,3,4]))

def extract_full_name(n):
	print(filter(lambda ns:ns['first'].join(ns['last']),n))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
from termcolor import colored
print(colored("HI THERE!",color="cyan"))