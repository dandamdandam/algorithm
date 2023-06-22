'''
1916
0.5초 128MB

N개의 도시, 한도시->다른도시 M개의 버스
도시의 번호는 1부터 N
A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화

N(1 ≤ N ≤ 1,000)
M(1 ≤ M ≤ 100,000)
(버스)출발지 도착지 비용(0<= <100,000)
출발지 도착지

최소비용출력
'''
import sys
import math
input=sys.stdin.readline

# 다익스트라
def dijkstra(a, b, graph):
    # 기본설정(방문, 시험적 거리 설정)
    visited=[False for _ in range(len(graph))]
    dist=[math.inf for _ in range(len(graph))]
    p=a # 현재 꼭짓점
    dist[p]=0

    while not visited[b]:
        for i in graph[p]:
            if not visited[i[0]]:
                dist[i[0]]=min(dist[i[0]], dist[p]+i[1])
        visited[p]=True
        # 미방문 중 가장 작은 시험적 거리 꼭짓점을 현위치로
        min_ind=0
        min_val=math.inf
        for i in range(len(graph)):
            if not visited[i]:
                if min_val>dist[i]:
                    min_val=dist[i]
                    min_ind=i
        if min_ind==b:
            break
        p=min_ind

    return dist[b]

# 입력받기
n=int(input())
m=int(input())
# 그래프 ex) [[ (2, 100), (1, 10) ], [], [], [ (0, 50) ]]
graph=[[] for _ in range(n)]
for _ in range(m):
    sta, des, wei=map(int, input().split())
    graph[sta-1].append((des-1, wei))
a, b=map(int, input().split())
a, b=a-1, b-1

print(dijkstra(a, b, graph))
