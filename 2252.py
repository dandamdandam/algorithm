'''
2252 2초 128MB

N명 학생 줄 세우기
두 학생의 키를 비교해 앞에 서야 할 학생이 A.

1: N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)
1+M: 두 학생의 번호 A, B (1~N)

줄을 세운 결과 출력
'''
import sys
from collections import deque

input=sys.stdin.readline
print=sys.stdout.write

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]  # 진입차수 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 1. 진입 차수가 0인 모든 노드를 큐에 넣는다.
que=deque()
for i in range(1, n+1):
    if indegree[i]==0:
        que.append(i)

# 2. 큐가 빌 때까지 반복
while que:
    # 1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
    cur = que.popleft()
    print(str(cur)+" ")
    for i in graph[cur]:
        indegree[i] -= 1
        # 2. 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.
        if indegree[i]==0:
            que.append(i)