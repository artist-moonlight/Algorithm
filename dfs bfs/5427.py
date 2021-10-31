from collections import deque
import sys
input = sys.stdin.readline

# 이동 좌표 설정
dx=[1,-1,0,0]
dy=[0,0,-1,1]
def bfs(): #BFS 탐색
    global queue,fire 
    while queue:
        hi=deque()#탐색할 임시 큐 생성
        #상구 이동 먼저 탐색
        while queue:
            x,y = queue.popleft()#x,y좌표 pop
            #각 끝좌표에 위치할 경우(탈출) start[x][y] 위치 리턴
            if (x == h - 1 or y == w - 1 or x == 0 or y == 0) and sanggu[x][y] != "*":
                return sanggu[x][y]
            #동,서,남,북 방향으로 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #이동할 위치가 이동 가능한 경우
                if 0 <= nx < h and 0 <= ny < w and sanggu[nx][ny] == "." and sanggu[x][y] != "*":
                    #위치 값 증가(이동거리)
                    sanggu[nx][ny] = sanggu[x][y] + 1
                    hi.append([nx, ny])#다음 탐색할 위치값 삽입 
        queue=hi#탐색할 queue에 hi가 가진 queue저장
        hi=deque()#hi초기화

        # 불이 번질 위치 bfs 탐색
        while fire:
            x,y =fire.popleft()#x,y좌표 pop
            #동,서,남,북 방향으로 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #불이 번질 위치가 이동 가능한 경우
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and sanggu[nx][ny] != "#":
                    #불 번짐
                    sanggu[nx][ny] = "*"
                    visited[nx][ny] = 1#방문 저장
                    hi.append([nx, ny])#다음 탐색할 위치값 삽입
        fire=hi#불 리스트에 hi가 가진 queue저장 
        
n=int(input()) #총 케이스 수 입력 (최대 100개)
for i in range(n): #n개의 맵 각각 입력
    w, h = map(int, input().split()) #너비 w 높이 h입력
    sanggu=[]#상구 이동 리스트
    fire=deque()
    queue=deque()
    visited = [[0] * w for i in range(h)]#방문 여부 체크리스트 초기화
    for j in range(h):
        a=list(input().strip())#문자 입력 받기 
        sanggu.append(a)
        for k in range(w):
            if a[k] == "@": #상근이가 시작할 위치 
                sanggu[j][k] = 0 
                queue.append([j, k])#queue 큐에 삽입
            elif a[k] == "*": #불의 위치
                fire.append([j, k])#fire 큐에 삽입
                visited[j][k]=1#불 위치 방문 체크
    result=bfs()
    print(result + 1 if result != None else "IMPOSSIBLE")
