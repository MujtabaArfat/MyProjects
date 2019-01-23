def count_dollar_signs(s):
	count = 0
	for i in s:
		if i=='$':
			count=count+1
	return count
print(count_dollar_signs("Me$$y"))