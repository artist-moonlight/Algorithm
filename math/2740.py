import sys
a=[]
n,m=map(int,sys.stdin.readline().split())
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
b=[]
m,k=map(int,sys.stdin.readline().split())
for _ in range(m):
    b.append(list(map(int,sys.stdin.readline().split())))
c=[[0 for _ in range(k)]for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j]+=a[i][l]*b[l][j]
for i in c:
    for j in i:
        print(j,end=' ')
    print()
