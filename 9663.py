'''
9663
10초 128MB

N*N 위에 퀀 N개를 서로 공격할 수 없게 놓는 문제
1<=N<15

경우의 수 출력
'''

# n=int(input())
# lo=[-1 for _ in range(n)] # 각 퀸의 위치. -1은 보드 바깥이라고 본다.
n=int(input())
row=[0 for _ in range(n)]

# def step(n_i):
#     '''
#     다음 칸 리턴
#     n_i번째 퀸은 n줄에서만 움직임
#     맨 끝에 다다랐다면 0리턴
#     @param n_i 옮길 퀸의 번호
#     '''
#     if lo[n_i]==n-1:
#         return -1
#     else:
#         return lo[n_i]+1
# def isSuit(n_i, y):
#     '''
#     현재 가려는 곳이 다른 퀸과 겹치거나 잡힐 위치이면 False
#     (가지치기)
#     '''
#     for i in range(n):
#         # 아직 놓지 않은 퀸과 자기자신은 비교에서 제외
#         if lo[i]!=-1 and i!=n_i:
#             # 대각선은 놓으려는 자리에서 x자리끼리 뺀 것==y자리 뺸 것이면 겹침
#             # y가 같으면 겹침 처리.
#             if lo[i]==y or abs(i-n_i)==abs(lo[i]-y):
#                 return False
#     return True

# isSuit랑 비슷한 코드
def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

# cnt=0
# def dfs(i):
#     # 마지막 퀸까지 보드 안에 놓임
#     global cnt
#     if lo[-1]>-1:
#         cnt+=1
#         return
    
#     lo[i]=step(i)
#     while not lo[i]==-1:
#         if isSuit(i, lo[i]):
#             dfs(i+1)
#         lo[i] = step(i)

ans=0
def n_queens(x):
    global ans
    if x==n:
        ans+=1
        return

    else:
        for i in range(n):
            row[x]=i
            if is_promising(x):
                n_queens(x+1)

# dfs(0)
# print(cnt)
n_queens(0)
print(ans)