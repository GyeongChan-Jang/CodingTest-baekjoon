import sys
input = sys.stdin.readline

# a: 양이 하루에 먹는 사료양
# b: 염소가 하루에 먹는 사료양
# n: 양, 염소 전체 수
# w: 전체 사료량
a, b, n, w = map(int, input().split())
answer = []
for i in range(1, n + 1):
  if a * i + (b * (n - i)) == w and n - i  > 0:
    answer.append([i, n - i])

if len(answer) > 1 or len(answer) == 0:
  print(-1)
else:
  print(*answer[0])
