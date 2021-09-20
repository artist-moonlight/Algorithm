import sys
n=int(sys.stdin.readline())
m=n
ok=False
for i in range(1,n):
    hi=[]
    for j in str(i):
        hi.append(int(j))
    total=sum(hi)+int(i)
    if total==m:
        print(int(i))
        ok=True
        break
if ok==False:
    print(0)
