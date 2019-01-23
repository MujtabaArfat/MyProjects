
def get_multiples(num1,num2):
    i=1
    while i<=num2:
        yield num1*i
        i=i+1
    if i>num2:
    	yield "StopIteration"
evens = get_multiples(2, 3)
print(next(evens)) # 2
print(next(evens)) # 4
print(next(evens)) # 6
print(next(evens))# StopIteration


