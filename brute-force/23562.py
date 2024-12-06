import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(n)]

min_cost = float('Inf')
# for k in range(1, min(n // 3 + 1, m // 3 + 1)):