array = [ 1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 , 1024 , 2048]
t = int( input() )
for i in range(t):
	count = 0
	value = int( input() )
	# print ("Initial Value : " + str(value) )
	while (value > 0):
		if(value >= array[11]):
			# print ("Value > 2048")
			value = value - array[11]
			count+=1
		else:
			for j in range (0 , 12):
				if (int(array[j]) > int(value)):
					count+=1
					# print ("Array Value : " + str(array[j]))
					# print ("Value : " + str(value))
					value = value - array[j-1]
					# print ("After Value : " + str(value) + "\n\n")
					break
	print (str(count))



