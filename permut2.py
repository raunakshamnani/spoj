t = int(input())

while (t != 0):

	l1 = []
	l2 = []

	l1 = list ( map( int, input().split() ) )

	for i in range(len(l1)):
		l2.append(0)

	for i in range(len(l1)):
		l2[l1[i]-1] = i+1

	if (l2 == l1):
		print ("ambiguous")
	else:
		print ("not ambiguous")

	t = int(input())
