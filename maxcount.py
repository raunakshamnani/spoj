from collections import Counter

t = int( input() )
while t:
	t = t - 1
	length = int( input() )
	array = list ( map( int, input().split() ) )
	array.sort()
	most_common,num_most_common = Counter(array).most_common(1)[0]
	print ( most_common , num_most_common)

