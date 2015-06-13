a,b = map( int, input().split() )
c = a - b
d = c%10
if (d > 5):
	c = c - 1
else:
	c = c + 1

print (c)
