t = int(input())

while t:
	t = t - 1
	j = 1
	value = int(input())
	count = 0
	while int(value/5**j)>0:
		count = count + int(value/5**j)
		j+=1
	print (str(count))
