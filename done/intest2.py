import sys
 
n, k = map(int, sys.stdin.readline().split())
 
count = 0
i = 1
t = []
while i <= n:
    item = int(raw_input())
    if item % k == 0:
        count += 1
    i += 1
 
print str(count)
 
