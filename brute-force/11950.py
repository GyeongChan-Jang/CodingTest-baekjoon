import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(N)]

min_value = float('Inf')
# 흰색, 파랑, 빨강 몇개의 줄 말고 끝 줄 대해 탐색
for w in range(1, N - 1):
    for b in range(w + 1, N):
        r = w + b
        print(f'흰: {w} 파: {b} 빨: {r}일 때')
        if r >= 1:
            cost = 0

            # 각각의 비용 계산
            # 흰색
            for i in range(w):
                cost += sum(1 for j in range(M) if matrix[i][j] != 'W')

            # 파랑
            for i in range(w, b):
                cost += sum(1 for j in range(M) if matrix[i][j] != 'B')

            for i in range(b, N):
                cost += sum(1 for j in range(M) if matrix[i][j] != 'R')

            min_value = min(min_value, cost)

print(min_value)

# 흰색, 파랑, 빨강 각각 몇개의 줄일 지에 대한 탐색 필요
# min_value = float('Inf')
#
# for w in range(1, N - 1):
#     for b in range(1, N - w):
#         r = N - w - b
#         if r >= 1:
#             print(f'흰: {w} 파: {b} 빨: {r}일 때')
#             cost = 0
#             # 각 영역의 비용 계산
#             # 흰색 영역
#             for i in range(w):
#                 for j in range(M):
#                     if matrix[i][j] != 'W':
#                         cost += 1
#
#             # 파랑 영역
#             for i in range(w, w + b):
#                 for j in range(M):
#                     if matrix[i][j] != 'B':
#                         cost += 1
#
#             # 빨강 영역
#             for i in range(w + b, N):
#                 for j in range(M):
#                     if matrix[i][j] != 'R':
#                         cost += 1
#
#             min_value = min(min_value, cost)
# print(min_value)




# for i in range(1, N):
#     for j in range(1, N):
#         for k in range(1, N):
#             if i + j + k == N:
#                 area = 0
#                 print(f'흰: {i} 파: {j} 빨: {k}일 때')

# 흰, 파, 빨
# N: 4, M: 5
# 1, 1, 2
# 1, 2, 1
# 2, 1, 1

# N: 6, M: 14
# 1, 1, 4
# 1, 2, 3
# 1, 3, 2
# 1, 4, 1
# 2, 1, 3
# 2, 2, 2
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
# 4, 1, 1