from sys import stdin

def mugging(no_of_notes , amount , value ):
	if (no_of_notes == 0 and amount > 0):
		return False
	elif (no_of_notes == 0):
		return True
	if (value[no_of_notes-1] > amount):
		return mugging(no_of_notes-1 , amount , value)
	return mugging(no_of_notes-1 , amount - value[no_of_notes-1] , value) or mugging(no_of_notes-1 , amount , value)

t = int( input() )

for i in range(t):
	no_of_notes , amount = map( int, input().split() )
	value = []
	for j in range(no_of_notes):
		value.append(int ( input() ))
	value.sort()
	# print (value)
	if mugging(no_of_notes , amount , value):
		print ("Yes")
	else:
		print ("No")

