import sys
input = sys.stdin.readline

N = int(input())

count = 0
for a in range(1, 501):
  for b in range(1, 501):
    if a * a == b * b + N:
      count += 1

print(count)