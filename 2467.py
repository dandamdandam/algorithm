'''
2467 1초 128MB

1: N은 2 이상 100,000
2: -1,000,000,000 이상 1,000,000,000 이하 오름차순

특성값의 오름차순으로 출력
'''
n=int(input())
arr=list(map(int, input().split()))

left=0
right=n-1
minGLeft=left
minGRight=right
while left<right:
    if abs(arr[minGLeft]+arr[minGRight]) > abs(arr[left]+arr[right]):
        minGLeft=left
        minGRight=right
    if abs(arr[left])<abs(arr[right]):
        right-=1
    else:
        left+=1

print(arr[minGLeft], arr[minGRight])