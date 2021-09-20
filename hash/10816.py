import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))

hashmap={}
for num in data:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1
m=int(sys.stdin.readline())
find=list(map(int,sys.stdin.readline().split()))
print(' '.join(str(hashmap[hi]) if hi in hashmap else '0' for hi in find))
