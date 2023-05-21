'''
N일간 임무 수행

장소, 임무종류 각각 고르되 하루 한가지만
장소 -> 수족관, 시청, 학교
임무종류 -> 정보수집, 감시

진척도
전날에 간 곳을 가면 절반의 진척도 얻음

기여도 = 진척도의 함

M 이상의 기여도를 얻을 수 있는 임무 수행방법개수 출력

N M
각 임무+장소 조합의 가능진척도
'''
# 중복순열 생성기
from itertools import product

N, M = map(int, input().split())
# 일차원배열로 가능진척도 받기
data = list(map(int, input().split()+input().split()))

# 주어진 일의 순서에 따른 진척도 계산
def calc(task):
    point=0
    # 이전에 방문한 장소
    # 수족관 0, 시청 1, 학교 2
    prev_place=None
    for i in task:
        if prev_place==i%3:
            point+=data[i]/2
        else:
            point+=data[i]
        prev_place=i%3
    return point

cnt=0
for i in product(range(6), repeat=N):
    if M<=calc(i):
        cnt+=1
print(cnt)
