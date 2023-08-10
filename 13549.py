'''
13549 2초 512MB

수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)
1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치

1: n k
가장 빠른 시간
'''
'''
5 7
2
5-10-9-18-17
'''
from collections import deque

class Pointer():
    def __init__(self, p, sec):
        self.p=p
        self.sec=sec

n, k=map(int, input().split())
MAX_I=max(n, k)*2+1
area=[MAX_I for _ in range(MAX_I)]
que=deque()

if n==k:
    area[k]=0
else:
    que.append(Pointer(n, 0))

while que:
    x=que.popleft()

    if x.p<<1 < MAX_I:
        if area[x.p<<1]>x.sec:
            area[x.p<<1]=x.sec
            if x.p<<1 != k:
                que.append(Pointer(x.p<<1, x.sec))
    if x.p+1 < MAX_I:
        if area[x.p+1]>x.sec+1:
            area[x.p+1]=x.sec+1
            if x.p+1 != k:
                que.append(Pointer(x.p+1, x.sec+1))
    if x.p-1 >= 0:
        if area[x.p-1]>x.sec+1:
            area[x.p-1]=x.sec+1
            if x.p-1 != k:
                que.append(Pointer(x.p-1, x.sec+1))


print(area[k])