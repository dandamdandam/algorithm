'''
6443 1s 128MB

입력받은 영단어로 만들 수 있는 모든 단어 출력. 알파벳 순서로 출력하기. 중복제거 필요.

1: N(단어의 개수)
n+1: 소문자로 이루어진 영단어(1~20길이, 애너그램 10000개 이하)

1. 무조건 백트래킹 사용해야겠다.
2. 뒤 요소(알파벳 순서, 중복제거)는 각각 다음과 같이 표현.
    1) 알파벳 순서: 처음 받을 때 정렬하고 시작
    2) 중복제거: 해당자리에서 고려한 적이 있는 값이면 넘어가기
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input())

    while n>0:
        n-=1
        
        s = sorted(input().strip())
        visited = [False for _ in range(len(s))]
        printing = [None for _ in range(len(s))]
        dfs(s, visited, printing, 0)

def dfs(s:str, visited: list[bool], printing: list[str], idx:int):
    if idx==len(s):
        print(''.join(printing)+'\n')
        return
    for i in range(len(s)):
        # printing 안에 없고, 중복요소가 아닐 때
        if not visited[i] and printing[idx]!=s[i]:
            printing[idx]=s[i]
            visited[i]=True
            dfs(s, visited, printing, idx+1)
            if idx+1 < len(s):          # 중복요소 채크를 위해 2개 이상 밀린 경우만 초기화
                printing[idx+1] = None
            visited[i]=False

if __name__ == '__main__':
    main()