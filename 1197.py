'''
1197 1초 128MB

1: 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)
1+E: A번 정점과 B번 정점이 가중치 C(절댓값 1,000,000이하)인 간선으로 연결

최소 스패닝 트리의 가중치 출력
'''
import sys
import heapq
input = sys.stdin.readline

# 입력받기
v, e=map(int, input().split())
graph = [[] for _ in range(v)]  # (가중치, 연결된 정점) 저장
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))
    graph[b-1].append((c, a-1))

# 1. 프림 알고리즘 기본설정
connected=[False for _ in range(v)] # 각 정점이 연결되어 있는가?
min_branch=[]                       # 연결된 간선의 최소힙
sum_w=0                             # 가중치 합
# 시작정점 => 0
connected[0]=True
for i in graph[0]:
    heapq.heappush(min_branch, i)

# 2. 연결된 간선 중 최소 가중치를 가진 간선 선택
# 3. n-1개의 간선이 선택될 때까지 반복
branch_cnt=0
while branch_cnt < v-1:
    next_w, next_n = heapq.heappop(min_branch)
    if not connected[next_n]:
        connected[next_n]=True
        for i in graph[next_n]:
            heapq.heappush(min_branch, i)
        sum_w+=next_w
        branch_cnt+=1

print(sum_w)