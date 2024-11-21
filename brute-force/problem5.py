# 모든 위치에서
# 모든 친구들의 거리를 계산
# 가장 짧은 거리 출력

# 한 곳에서 모일 때, 비용을 최소화 하기 위해서는
# 우리 중 한 곳에서 모이면 된다.
n = int(input())
arr = []
arr_y = []
arr_x = []
answer = [-1] * n
dist_all = []  # 모든 거리를 저장할 리스트

# 1. 입력 받기
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    arr_y.append(b)
    arr_x.append(a)

# 2. 모든 가능한 목적지에 대한 거리 계산
for y in arr_y:
    for x in arr_x:
        dist = []    
        for ex, ey in arr:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)
        dist_all.append(sorted(dist))  # 정렬된 거리를 저장

# 3. 최소 이동 횟수 계산
for distances in dist_all:
    tmp = 0
    for i in range(len(distances)):
        tmp += distances[i]
        if answer[i] == -1:
            answer[i] = tmp
        else:
            answer[i] = min(tmp, answer[i])
print(dist_all)
print(*answer)

