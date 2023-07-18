'''
15649
1초 512MB

참고: https://jiwon-coding.tistory.com/21

3 3
1
    1 2
        1 2 3 ->
    1 3
        1 3 2 ->
2
    2 1
        .....
'''

n,m = list(map(int,input().split()))

s = []
 
def dfs():
    # m의 길이를 만족해 하나의 수열이 만들어지면 재귀 탈출
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        # 한 수열에 겹치는 글자가 없어야 함
        if i not in s:
            s.append(i)
            dfs()
            # 출력 후 대입했던 수열 빼기
            s.pop()
 
dfs()