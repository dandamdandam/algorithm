'''
정수 n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램
0<n<11
'''
import sys
input = sys.stdin.readline

T = int(input())

# f(n) = f(n-1) + f(n-2) + f(n-3)
df = [1, 2, 4]
for i in range(3, 10):
    df.append(df[i-1]+df[i-2]+df[i-3])

s=[]
for _ in range(T):
    s.append(str(df[int(input())-1]))
print('\n'.join(s))
