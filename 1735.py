'''
1735 1초 256MB
다익스트라+최소힙!!

1: n(정점의 개수) e(간선의 개수) (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
2: k(시작 정점의 번호 1~v)
3+e: u v w (u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻) (u와 v는 서로 다르며 w는 10 이하의 자연수)

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력. 시작점 자신은 0. INF(경로 없음)
'''
import sys
import math
import heapq

input=sys.stdin.readline
print=sys.stdout.write

n, e=map(int, input().split())
k=int(input())

# 그래프 만들기
class Branch():
    def __init__(self, v, w):
        self.v=v
        self.w=w
    def __str__(self):
        print(str(self.v)+" "+str(self.w)+"\n")

graph=[[] for _ in range(n+1)]  # 0은 빈칸. 각 정점에 Branch의 리스트가 들어감.
dist=[math.inf for _ in range(n+1)] # 시각정점~각정점 거리 저장
for i in range(e):
    u, v, w=map(int, input().split())
    graph[u].append(Branch(v, w))

# 다익스트라
heap=[]
heapq.heappush(heap, (0, k))
visited=[False for _ in range(n+1)] # 이전방문여부
while heap:
    cur_dist, cur=heapq.heappop(heap)

    if visited[cur] or dist[cur]<cur_dist:
        continue

    dist[cur]=cur_dist
    visited[cur]=True
    for i in graph[cur]:
        if not visited[i.v]:
            dist[i.v]=min(dist[i.v], cur_dist+i.w)
            heapq.heappush(heap, (dist[i.v], i.v))

for i in range(1, n+1):
    if dist[i]==math.inf:
        print("INF\n")
    else:
        print(str(dist[i])+"\n")