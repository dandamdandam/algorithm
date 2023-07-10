'''
12865
2초 512MB

1:      N(물건 개수:100) K(최대 무게:100,000)
N+1:    W(무게) V(가치)

최대 가치합
'''

n, k=map(int, input().split())
'''
행에 담을 물건, 열에 최대 무게를 적은 dp.
특정 셀의 값 = 행번호만큼 물건이 있을 때 열번호 이하 무게로 담은 최대 가치
'''
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    w, v=map(int, input().split())
    if w<=k:
        dp[i+1][w]=v

for i in range(1, n+1):
    occupied=True
    v, w=0, 0
    for j in range(1, k+1):
        if occupied:
            if dp[i][j]==0:
                dp[i][j]=dp[i-1][j]
            else:
                occupied=False
                w=j
                v=dp[i][j]
                dp[i][j]=max(dp[i-1][j], v+dp[i-1][j-w])
        else:
            dp[i][j]=max(dp[i-1][j], v+dp[i-1][j-w])

print(dp[n][k])