import sys

n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data.sort()
m=int(sys.stdin.readline())
find=list(map(int,sys.stdin.readline().split()))
def binary(data,left,right,num):
    if left>right:
        return 0
    mid=(left+right)//2
    if num<data[mid]:
        return binary(data,left,mid-1,num)
    elif num>data[mid]:
        return binary(data,mid+1,right,num)
    else :
        return 1

for num in find:
    left=0
    right=n-1
    print(binary(data,left,right,num))
    

              
    
