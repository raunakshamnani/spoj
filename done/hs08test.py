import sys

withdraw , balance = input().split()
withdraw = float(withdraw)
balance = float(balance)
if ( (withdraw%5 == 0) and (balance > withdraw+0.5) ):
	print (balance - withdraw - 0.5)
else:
	print (balance)
