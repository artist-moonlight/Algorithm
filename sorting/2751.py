import sys
n=int(sys.stdin.readline())
data=[]
for i in range(n):
    hi=int(sys.stdin.readline())
    data.append(hi)
data.sort()
for num in data:
    print(num)
    
