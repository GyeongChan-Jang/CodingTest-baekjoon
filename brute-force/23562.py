import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a, b = map(int, input().split())

arr = [[0 for j in range(N)] for i in range(M)]

for i in range(M):
  string = input()
  print(string)

  for j in range(N):
    if string[j] == '#':
      print(string[j])
      arr[i][j] == 1
    else:
      arr[i][j] == 0

print(arr)