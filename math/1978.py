import sys
n=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
answer=0
for num in numbers:
    hi=True
    if num>1:
        for i in range(2,num):
            if num%i==0:
                hi=False
        if hi==True:
            answer+=1
print(answer)
