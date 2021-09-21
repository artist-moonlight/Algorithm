import sys
n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

left=1
right=max(data)
#정답인 최대값
result=0
while left<=right:
    answer=0
    mid=(left+right)//2
    #for num in data:
        #if num>mid:
            #answer+=num-mid
    answer=sum(num-mid if num>mid else 0 for num in data)
    if answer>=m:
        result=mid
        left=mid+1
    else :
        right=mid-1
print(result)
