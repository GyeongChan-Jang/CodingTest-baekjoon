import sys
input = sys.stdin.readline

mushrooms = [int(input().strip()) for _ in range(10)]

# 100을 처음으로 넘는 시점과 그 이전 지점을 비교하여 total 업데이트

total = 0
result = 0

for i, value in enumerate(mushrooms):
  total += value

  if total == 100:
    result = 100
    break

  
  if total - 100 == 100 - (total - mushrooms[i]): 
    result = max(total, total - mushrooms[i])
    break


  if len(str(total)) ==3:
    result = min(total, mushrooms[i])
    break
  
  # result = total

print(result)






# mushrooms = [int(input().strip()) for _ in range(10)]
# total = 0
# # 100을 처음으로 넘는 시점과 그 이전 지점을 비교하여 total 업데이트
# min_value = 0
# for i, value in enumerate(mushrooms):
#   if len(str(total)) == 3:
#     if total == 100:
#       min_value = total
#       break
      
#     if total - 100 == 100 - (total-mushrooms[i - 1]):
#       min_value = max(total, total-mushrooms[i - 1])
#     else:
#       min_value = min(total, total - mushrooms[i - 1])
#     break
#   total += value

# print(min_value)