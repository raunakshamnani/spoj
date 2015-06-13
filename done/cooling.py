t = int( input() )

while t:
	t = t - 1
	count = 0
	pie = []
	rack = []
	length = int( input() )
	pie = list ( map( int, input().split() ) )
	rack = list ( map( int, input().split() ) )
	pie.sort()
	rack.sort()
	# print (pie)
	# print (rack)

	for i in range(length):
		for j in range(length):
			if pie[i] <= rack[j]:
				count+=1
				rack[j] = -1
				break
	print (count)

