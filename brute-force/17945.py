import sys
input = sys.stdin.readline

A, B = map(int, input().split())

# with open('input.txt', 'r') as f:
#   A, B = map(int, f.readline().strip().split())

for i in range(-1000, 1001):
  if i * i + 2 * A * i + B == 0:
    print(i, end=" ")