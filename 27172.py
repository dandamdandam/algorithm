'''
27172 1초 1024MB

승리(+1). 패배(-1).
패배자%승리자==0.
모두 다른 플레이어와 한 번씩 비교하기.

1: N(2이상 100,000이하, 플레이어 수)
2:  각 플레이어가 가지고 있는 카드에 적힌 정수(중복 없음, 1이상 1,000,000 이하)

게임 종료 후 각 플레이어의 점수 출력
'''
n=int(input())
cards=list(map(int, input().split()))   # 각 플레이어가 가지고 있는 카드번호 저장.
score=[0 for _ in range(n)]             # 각 플레이어 점수 저장.
num_range=[-1 for _ in range(1000001)]  # 각 카드번호에 플레이어 번호 저장. -1: 존재X.

for i in range(n):
    num_range[cards[i]]=i

for i in range(n):
    # i번째 카드의 배수에 해당하는 카드가 존재하는가?
    for j in range(cards[i]*2, 1000001, cards[i]):
        if num_range[j] > -1:
            score[num_range[j]]-=1
            score[i]+=1

print(' '.join(map(str, score)))