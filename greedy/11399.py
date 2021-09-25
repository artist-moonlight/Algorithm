import sys
n=int(sys.stdin.readline())
time=list(map(int,sys.stdin.readline().split()))
time.sort()
total=0
wait=0
for num in time:
    wait+=num
    total+=wait
print(total)
