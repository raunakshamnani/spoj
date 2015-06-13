import sys

n , k = [int(i) for i in sys.stdin.readline().rstrip().split()]

divisible = 0
for i in range(n):
	value = int(sys.stdin.readline())
	if( value % k == 0):
		divisible+= 1
print (divisible)
