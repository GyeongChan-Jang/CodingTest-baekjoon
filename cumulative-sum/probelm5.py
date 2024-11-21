import sys
input = sys.stdin.readline

with open('input.txt', 'r') as f:
  # N: 동굴의 길이
  # H: 동굴의 높이
  N, H = map(int, f.readline().strip().split())
  obstacles = [int(f.readline().strip()) for _ in range(N)]

# 구간별로 겹치는 장애물의 개수 세기

sections = [i for i in range(H)]
print(sections)