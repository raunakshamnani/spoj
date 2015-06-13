t = int( input() )
while t:
	t = t - 1
	length = int( input() )
	array = list ( map( int, input().split() ) )
	array.sort()

	num = 0
	value = 0

	for i in range(length):
		temp = array.count(array[i])
		if (temp > num):
			num = temp
			value = array[i]
	print (value , num)


