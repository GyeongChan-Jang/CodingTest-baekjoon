import sys
input = sys.stdin.readline

N = int(input())

count = 0

for i in range(1, N): # 택희
  for j in range(1, N): # 영훈
    for k in range(1, N): # 남규
      if k > j + 1 and i != 0 and j != 0 and k != 0 and i % 2 == 0 and i + j + k == N:
        count += 1

print(count)