'''
1351 2s 128MB

A0 = 1
Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
N, P와 Q가 주어질 때, A_N을 구하는 프로그램 작성하기

p=2, q=3일 때
a1 = a(1/2) + a(1/3) = a0 + a0 = 2
a2 = a(2/2) + a(2/3) = a1 + a0 = 3
.
.

1. bfs + 동적 프로그래밍 생각해서 배열을 씀
2. n이 너무 커서 메모리 초과 실패
3. DP를 없애봄 -> 시간 초과 실패
4. 결국 서치 후 map 사용
**DP를 쓴 예상 시간 측정 필요**
'''
n, p, q = map(int, input().split())
A = {0: 1}

def getA_n(n: int):
    if(n in A):
        return A[n]
    else:
        A[n] = getA_n(int(n/p)) + getA_n(int(n/q))
        return A[n]

print(getA_n(n))