import sys
n=int(sys.stdin.readline())
time=[list(map(int, sys.stdin.readline().split())) for i in range(n)] 
time=sorted(time, key= lambda x: (x[1], x[0]))
cnt=0
answer=1
for num in time:
    if cnt==0:
        end=num[1]
        cnt+=1

    elif end!=num[1] and end<=num[0]:
        end=num[1]
        answer+=1

    elif end==num[0] and end==num[1]:
        answer+=1
print(answer)
