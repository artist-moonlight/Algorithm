import sys
n,k=map(int,sys.stdin.readline().split())
data=[]
for _ in range(n):
    hi=int(sys.stdin.readline())
    data.append(hi)
data.sort(reverse=True)
answer=0
for num in data:
    if num<=k:
        answer+=k//num
        k=k%num
print(answer)
            
