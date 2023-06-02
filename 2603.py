'''
정사각형
파란색 1, 하얀색 0

4개의 N/2, N/2 종이로 나누기

N(2, 4, 8, 16, 32, 64, 128)
--
하얀색 개수
파란색 개수
'''
import sys
input= sys.stdin.readline

n=int(input())
paper=[list(map(int, input().split())) for _ in range(n)]

def allis(x, y, size):
    '''
    paper의 범위 내 정사각형의 색이 모두 흰/파랑인가?
    return 0(흰), 1(파), -1(같지 않음)
    '''
    assume=paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if assume!=paper[i][j]:
                return -1
    return assume
def quarter(x, y, size):
    '''
    현재 범위 내의 색이 같아질 때까지 4등분
    '''
    tmp=allis(x, y, size)
    if tmp==-1:
        size=size//2
        quarter(x, y, size)
        quarter(x+size, y, size)
        quarter(x, y+size, size)
        quarter(x+size, y+size, size)
    else:
        if tmp==1:
            cnt[1]+=1
        else:
            cnt[0]+=1

cnt=[0, 0]    # white, blue
quarter(0, 0, n)
print(cnt[0])
print(cnt[1])
