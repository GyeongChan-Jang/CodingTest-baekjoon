n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefixSum = [0 for _ in range(n + 1)]

for i in range(n):
  prefixSum[i + 1] = prefixSum[i] + nums[i]

answer = []
for j in range(k, n + 1):
  answer.append(prefixSum[j] - prefixSum[j - k])

print(max(answer))