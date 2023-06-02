'''
AC언어 -> 정수배열에 연산

함수 R(뒤집기)과 D(버리기)
함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, 
D는 첫 번째 수를 버리는 함수
비어있는데 D사용시 에러

T(100 이하)
p(수행할 함수. 1<=길이<=100,000)
n(배열에 들어있는 정수개수. 0<=n<=100,000)
[x1,...,xn] (1 ≤ xi ≤ 100)
'''
import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write

T=int(input())
for _ in range(T):
    direc=input().rstrip()
    n=int(input())
    if n:
        que=deque( list(map(int, input()[1:-2].split(','))) )
    else:
        input()
        que=deque()
    error=False
    reverse_n=0   # 몇번 뒤집어 졌는가
    for i in direc:
        if i=='R':
            reverse_n+=1                                                                                                                                                                                                                                                                                                                                                                                                                
        else:
            if que:
                if reverse_n%2==0:
                    que.popleft()
                else:
                    que.pop()
            else:
                error=True
                break
    if error:
        print('error\n')
    else:
        if reverse_n%2==1:
            que.reverse()
        print('['+','.join(map(str, que))+']\n')
