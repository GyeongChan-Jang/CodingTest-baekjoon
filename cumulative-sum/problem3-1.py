import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# with open('input.txt', 'r') as f:
#     n = int(f.readline().strip())
#     arr = [list(map(int, f.readline().strip().split())) for _ in range(n)]

list = [0 for _ in range(1001)]
maxHeight = maxIndex = 0

for [L, H] in arr:
  # L 위치에 H 기록
  list[L] = H
  # maxIndex 구하기

  if maxHeight < H:
    maxHeight = H
    maxIndex = L
  
# 왼쪽부터 처리
answer = maxHeight = 0
for i in range(maxIndex + 1):
  maxHeight = max(maxHeight, list[i])
  answer += maxHeight

# 오른쪽 처리
maxHeight = 0
for i in range(1000, maxIndex, -1):
  maxHeight = max(maxHeight, list[i])
  answer += maxHeight

print(answer)