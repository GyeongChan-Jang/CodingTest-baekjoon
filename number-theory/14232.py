import sys
input = sys.stdin.readline

# 소인수 구하기!
k = int(input())

x = k
answer = []
for i in range(2, k + 1):
    if i * i > k:
        break

    while x % i == 0:
        answer.append(i)
        x //= i

if x != 1:
    answer.append(x)

print(len(answer))
print(*answer)