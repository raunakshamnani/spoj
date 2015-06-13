from sys import stdin

value = list( map( int, stdin.read().split()[1:] ) )
value.sort()

print("\n".join( map( str, value ) ) )  
