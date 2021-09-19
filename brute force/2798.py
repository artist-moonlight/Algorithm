
import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answer=-1
li=[]
ssum=0
mmax=0

for i in range(n):
    for j in range (i+1,n):
        for k in range(j+1,n):
            ssum=a[i]+a[j]+a[k]
            li.append(ssum)
            if ssum<=m and ssum>mmax :
                mmax=ssum
li.sort()        
print(mmax)
