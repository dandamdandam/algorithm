'''
5721 1s 256MB

여러개의 테스트케이스 (보초값: 0 0)
1: M N (1 ≤ M * N ≤ 10^5)
m+1: 박스에 들어있는 사탕의 개수 n개 (1~10^3)

하나 고르면 위 아래 행과 양옆 셀 삭제

1. DP를 사용할 수 있을까? (최적원리)
(한 줄 내의) 가장 큰 것 고르기: 10 12 10 2 1 (최적: 21) -> 0 0 0 2 1 (12) -> 0 0 0 0 0 (14) -> x
(차례로 가며) 3개씩 최적 고르기: 10 12 10 20 1 (최적: 32)
더 이상 생각해내게 귀찮아서 그냥 백트래킹 하기로 함

2. 그리디 -> 백트래킹을 설계하자!
    1) state space tree
        0행 선택, 행 내 최대 합 산출 및 누적
        그 다음 가능한 행 선택, 행 내 최대 합 산출 및 누적
        n행까지 돌고 현재 값 저장. 및 백 후 다시 산출 및 누적
        a) 행 내 최대 합 산출
            1과 같이 진행(행 내 최대 합 산출 -> 해당 셀 사탕 수

3. 최적원리 개념을 까먹은 듯함... 생각해보니까 뒤를 결정하는데 저 앞부분의 값은 영향을 주지 않고, 최대여야 하니 DP가 맞는 거였다.
    - 활용은 이렇게 -> i번째 요소를 판단할 때, i를 선택하지 않는 경우(i-1이전의 최적값)과 i를 선택하는 경우(i-2이전의 최적값)을 비교해 선택한다.
'''
import sys

def main():
    input = sys.stdin.readline
    # print = sys.stdout.write
    run = True

    while(run):
        m, n = map(int, input().split())
        if m==0:
            run = False
            break

        row_sum = [0 for _ in range(m)]     # 각 행의 최대 합
        dp = [0 for _ in range(n)] # dp
        for i in range(m):
            row = list(map(int, input().split()))
            row_sum[i] = dp_func(row)
            # dp 초기화
            for i in range(n):
                dp[i] = 0
        
        # 열의 최대 합
        dp = [0 for _ in range(m)]
        print(str(dp_func(row_sum)))

def dp_func(arr: list[int]) -> int:
    """특정 조건을 단 arr 최대 합을 구하는 DP 함수
    특정 조건: 더하는 요소들이 연속되어 있으면 안됨

    arr: 더할 요소가 담겨있는 배열
    return -> 최대 합
    """
    dp = [0 for _ in range(len(arr)+1)]
    dp[1] = arr[0]
    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i-1])
    return dp[len(arr)]
    
if __name__ == '__main__':
    main()