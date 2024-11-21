import sys
input = sys.stdin.readline

# 7개의 합이 100
heightArr = [int(input().strip()) for _ in range(9)]
totalSum = sum(heightArr)

for i in range(9):
  for j in range(i + 1, 9):
      if totalSum - (heightArr[i] + heightArr[j]) == 100:
        filteredArr = filter(lambda x: x != heightArr[i] and x != heightArr[j], heightArr)
        print(*sorted(filteredArr), sep="\n")  # 오름차순 정렬 후 출력
        exit()