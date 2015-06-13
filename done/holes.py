t = int(input())
while t:
	t = t - 1
	value = input()
	count = 0
	for char in value:
		if char in "QROPDA":
			count+=1
		if char in "B":
			count+=2
	print (count)
