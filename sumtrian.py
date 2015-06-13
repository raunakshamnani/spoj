t = int(input())

while t:
	t = t - 1
	length = int( input() )
	value = []

	for i in range(length):
		value.append( list( map( int, input().split() ) ) )

	# print (value)
	# print (length)

	for i in range(length-1 , 0 , -1):
		# print ("i : " + str(i))
		for j in range(i):
			# print ("j : " + str(j))
			value[i-1][j] = value[i-1][j] + max(value[i][j] , value[i][j+1])

	print (value[0][0])
