import sys
n,c=map(int,sys.stdin.readline().split())
data=[]
for _ in range(n):
   hi=int(sys.stdin.readline())
   data.append(hi)
data.sort()
#최소거리 1
left=1
#최대거리
right=data[n-1]-data[0]
while left<=right :
    mid=(left+right)//2
    cnt=1
    #배열에서 거리 차이 계산
    hi=data[0]
    for i in range(1,n):
        if data[i]-hi>=mid:
            cnt+=1
            hi=data[i]      
    if cnt>=c:
        answer=mid
        left=mid+1
    else :
        right=mid-1
print(answer)
