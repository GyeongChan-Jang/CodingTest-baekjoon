# import sys
# input = sys.stdin.readline

# H, W = map(int, input().split())
# arr = list(map(int, input().split()))

with open('input.txt', 'r') as f:
    H, W = map(int, f.readline().strip().split())
    arr = list(map(int, f.readline().strip().split()))

# maxIndex와 maxHeight를 찾고
# maxHeight를 기준으로 왼쪽, 오른쪽으로 나눠서 H를 계산
list = [0 for _ in range(501)]

maxIndex = maxHeight = 0

for i in range(W):
  list[i] = arr[i]
  if arr[i] > maxHeight:
    maxHeight = arr[i]
    maxIndex = i

answer = maxHeight = 0
# 왼쪽 처리
for i in range(maxIndex):
  maxHeight = max(maxHeight, list[i])
  answer += maxHeight - list[i]

maxHeight = 0
for i in range(500, maxIndex, -1):
  maxHeight = max(maxHeight, list[i])
  answer += maxHeight - list[i]

print(answer)