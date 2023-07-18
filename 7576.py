'''
7576
1초 256MB

N*M에 토마토를 하나씩 보관
익은 토마토/안익은 토마토
익은 토마토는 왼/오/위/아래의 안익은 토마토를 익게 함(하루걸림)
창고의 모든 토마토가 익는 최소 일수

2 ≤ M,N ≤ 1,000
1->익은 토마토
0->안익은 토마토
-1->비어있음

최소일수 출력
모든 토마토를 익힐 수 없을 때 -1
'''
import sys
from collections import deque

input=sys.stdin.readline

N, M = map(int, input().split())
N, M = M, N
barn = []
for _ in range(N):
    barn += list(map(int, input().split()))

# bfs 1, 2, 3

# 1. 탐색 시작 노드를 큐에 넣고 방문 처리 하기
visited = [False for _ in range(N*M)]       # 익은 토마토가 있거나 비어있으면 방문처리
que = deque()                               # 익은 토마토가 있으면 큐에 저장
for i, val in enumerate(barn):
    if val!=0:
        visited[i]=True
        if val==1:
            que.append(i)
que.append(-1)      # 일자 나눔
days = 0            # 걸린 일수

# 이동할 인덱스가 유효한가?
def isValid(index, dx, dy):
    return 0 <= index//M+dx < N and 0 <= index%M+dy < M
# 방문하지 않은 노드를 큐에 넣고 방문 처리
def dfs_helper(index):
    if not visited[index]:
        que.append(index)
        visited[index]=True

# 3. 큐가 빌 때까지 반복
while True:
    days+=1
    # 2. 큐에서 노드를 꺼내고 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 넣고 방문 처리
    cur=que.popleft()
    # -1로 하루치 번짐 측정
    while cur > -1:
        # 위 아래 왼 오
        if isValid(cur, -1, 0):
            dfs_helper(cur-M)
        if isValid(cur, 1, 0):
            dfs_helper(cur+M)
        if isValid(cur, 0, -1):
            dfs_helper(cur-1)
        if isValid(cur, 0, 1):
            dfs_helper(cur+1)
        cur=que.popleft()
    if que:
        que.append(-1)
    else:
        break
        
if sum(visited)==len(visited):
    print(days-1)
else:
    print(-1)
