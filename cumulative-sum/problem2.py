# import sys
# input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 구간이 따로 정해지지 않음
# 구간의 합 중 가장 큰 값 출력

prefixSum = [0 for _ in range(n + 1)]

for i in range(n):
  # 누적합과 현재의 값 중 큰 값으로 prefixSum 업데이트
  # 누적합 보다 현재 값이 더 크다면 현재부터 다시 연속해서 더하기
  prefixSum[i + 1] = max(prefixSum[i] + nums[i], nums[i])

print(max(prefixSum))