t = int( input() )
while t:
	t = t - 1
	value = input()
	operation = []
	val = []
	for i in range( len(value) ):
		if (value[i] == '('):
			continue
		elif (value[i] in '+-*/^'):
			operation.append(value[i])
		elif (value[i] == ')'):
			a = val.pop()
			b = val.pop()
			c = operation.pop()
			extra = b + a + c
			# print (extra)
			val.append(extra)
		else:
			val.append(value[i])
	print (val.pop())
