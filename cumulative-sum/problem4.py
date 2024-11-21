import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# positions = [list(map(int, input().split())) for _ in range(M)]

with open('input.txt', 'r') as f:
    N, M = map(int, f.readline().strip().split())
    matrix = [list(map(int, f.readline().strip().split())) for _ in range(N)]
    positions = [list(map(int, f.readline().strip().split())) for _ in range(M)]

prefix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for y in range(N):
  for x in range(N):
    prefix[y + 1][x + 1] = prefix[y + 1][x] + prefix[y][x + 1] - prefix[y][x] + matrix[y][x]

answer = []
for x1, y1, x2, y2 in positions:
  total = (prefix[x2][y2] - prefix[x2][y1 - 1] - prefix[x1 - 1][y2] + prefix[x1 - 1][y1 - 1])
  answer.append(total)

print(*answer, sep='\n')