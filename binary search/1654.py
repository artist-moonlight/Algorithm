import sys
k,n=map(int,sys.stdin.readline().split())
data=[]
for _ in range(k):
    hi=int(sys.stdin.readline())
    data.append(hi)
left=1
right=max(data)
#랜선의 최대 길이
d=0
while left<=right:
    mid=(left+right)//2
    answer=0
    for num in data:
        answer+=num//mid
    if answer>=n:
        d=mid
        #최대길이를 구해야 하기 때문에
        left=mid+1
    else:
        right=mid-1
print(d)
