import sys
n=int(sys.stdin.readline().strip())
for _ in range(n):
    rd=sys.stdin.readline().strip()
    change=int(sys.stdin.readline().strip())
    li=sys.stdin.readline().strip()[1:-1]
    if li:
        li=li.split(',')
    else:
        li=[]
    reverse=False
    error=False
    for order in rd:
        if order=='R':
            reverse=not reverse
        elif order=='D':
            if len(li)==0:
                error=True
                break
            elif reverse:
                li.pop()
            else:
                li.pop(0)
    if error:
        print('error')
    else:
        if reverse:
            li.reverse()
        ret=','.join(li)
        print(f'[{ret}]')
