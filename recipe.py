from fractions import gcd
from functools import reduce

t = int( input() )

for i in range (t):
	value = list ( map( int, input().split()[1:] ) )
	hcf = reduce (gcd , value)
	# print (hcf)
	newList = [int(x / hcf) for x in value]
	print(" ".join( map( str, newList ) ) )
