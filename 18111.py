'''
세로 N, 가로 M 집터. 왼쪽 위 좌표 (0, 0)
초기 인벤토리 블록개수 B

작업
1. (2초)블록 제거 후 인벤토리에 넣기
2. (1초)인벤토리에서 블록을 꺼내 설치

최소 시간과 그런경우 땅의 높이

(1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7)
땅의 높이는 256보다 작거나 같은 자연수 또는 0
1초 1024MB

전체 블록 수 + b의 평균 -> 최대높이
최소 블록의 수 -> 최소높이 
'''
import sys
input = sys.stdin.readline

N, M, b = tuple(map(int, input().split()))
site = [list(map(int, input().split())) for _ in range(N)]

def cal_time(hi):
    time=0
    time_2=0
    for i in site:
        for j in i:
            if hi<=j:
                time_2+=j-hi
            else:
                time+=hi-j
    return time+time_2*2

max_h=0
min_h=256
for i in range(N):
    max_h+=sum(site[i])
    min_h=min(min_h, min(site[i]))  # 땅의 최소 높이
max_h=min((max_h+b)//(N*M), 256)     # 땅의 최대 높이

min_time=cal_time(min_h)            # 최소 시간
cur_hi=min_h                        # 최소 시간일 때의 땅의 높이
min_h+=1
for i in range(min_h, max_h+1):
    cur_time = cal_time(i)
    # 최소시간 갱신
    if cur_time <= min_time:
        min_time=cur_time
        cur_hi=i

print(min_time, cur_hi)
