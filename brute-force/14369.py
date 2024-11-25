import sys
input = sys.stdin.readline

N = int(input())
phone_nums = [input().strip() for i in range(N)]

alphabet_arr = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
alphabet_num_dict = {word: idx for idx, word in enumerate(alphabet_arr)}

results = []

for phone_num in phone_nums:
  num_count = {word: 0 for word in alphabet_arr}
  copy = phone_num

  # 알파벳의 고유 문자 기반 제거
  unique_keys = {'Z': 'ZERO', 'W': 'TWO', 'U': 'FOUR', 'X': 'SIX', 'G': 'EIGHT', 'O': 'ONE', 'T': 'THREE', 'F': 'FIVE', 'S': 'SEVEN', 'N': 'NINE'}

  for key, word in unique_keys.items():
    while key in copy:
      num_count[word] += 1
      for char in word:
        copy = copy.replace(char, '', 1)
  
  result = []
  for word, count in num_count.items():
    result.extend([alphabet_num_dict[word]] * count)
  results.append("".join(map(str, sorted(result))))

for i, res in enumerate(results, start=1):
  print(f"Case #{i}: {res}")

# alphabet_arr = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
# alphabet_num_dict = {
#   'ZERO': 0,
#   'ONE': 1,
#   'TWO': 2,
#   'THREE': 3,
#   'FOUR': 4,
#   'FIVE': 5,
#   'SIX': 6,
#   'SEVEN': 7,
#   'EIGHT': 8,
#   'NINE': 9
# }

# phone_string = []

# for phone_num in phone_nums:
#   num_arr = []
#   copy = phone_num
#   for alphabet in alphabet_arr:
#     count = 0
#     for a in alphabet:
#       if not a in copy:
#         copy = phone_num
#         break
#       else:
#         copy = copy.replace(a, '', 1)
#         count += 1

#     if count == len(alphabet):
#       num_arr.append(alphabet)
  
#   # 중복 검사
#   arr = []
#   dup = phone_num
#   while dup != "":
#     for string in num_arr:
#       if dup == "":
#         break
#       count = 0
#       for s in string:
#         dup = dup.replace(s, '', 1)
#         count += 1
      
#       if count != 0 and count % len(string) == 0:
#         arr.append(alphabet_num_dict[string])
#   phone_string.append(sorted(arr))

# result = ""
# for i, phone in enumerate(phone_string):
#   result = "".join(map(str, phone))
#   print(f"Case #{i + 1}: {result}")















# for phone_num in phone_nums:
#   including_nums = []
#   for alphabet in alphabet_arr:
#       if all(a in phone_num for a in alphabet):
#         including_nums.append(alphabet)
#   num_arr.append(including_nums)

#   count = 0

#   num_list = []
#   for num in including_nums:

#     copy = phone_num

#     while copy != "":
#       for n in num:
#         copy.replace(n, '', 1)
#         count += 1
    
#     if count != 0 and count % len(num) == 0:
#       num_list.append(num)
  
#   print(num_list)

















# answer = []

# for phone_num in phone_nums:
#   including_nums = []
#   copy = phone_num

#   for alphabet in alphabet_arr:
#     count = 0
#     print(f"{alphabet}랑 비교")
#     # while copy == "":
#     for a in alphabet:
#       if not a in copy:
#         print(f"Char {a} not in {copy}, breaking.")
#         copy = phone_num
#         break
#       else:
#         copy = copy.replace(a, '', 1)
#         count += 1
#         print(f"Current char: {a}, Updated copy: {copy}, Count: {count}")

#     if count != 0 and count % len(alphabet) == 0:
#       print(f"Alphabet {alphabet} is in {phone_num}.")
#       including_nums.append(alphabet)
    
#   answer.append(including_nums)
#   print(copy)

# print(answer)


# 몇번 등장하는지도 중요하기 때문에 안됨: "if all(a in copy for a in alphabet):"
# answer = []

# for phone_num in phone_nums: 
#   copy = phone_num
#   including_nums = []

#   while copy != "" :
#     for alphabet in alphabet_arr:
#       if all(a in copy for a in alphabet):
#         print(f"{alphabet}이랑 비교!")
#         including_nums.append(alphabet)
#         for a in alphabet:
#           copy = copy.replace(a, '', 1)

#   answer.append(including_nums)

# print(answer)

# for phone_num in phone_nums:
#     including_nums = []
#     copy = phone_num

#     # 숫자를 찾을 수 있을 때까지 반복
#     while copy:
#         found = False  # 숫자를 찾았는지 여부를 추적
        
#         # alphabet_arr에서 하나씩 돌면서 해당 문자열이 포함되어 있으면 처리
#         for alphabet in alphabet_arr:
#             if all(a in copy for a in alphabet):  # 알파벳이 모두 존재하면
#                 including_nums.append(alphabet)  # 해당 숫자 문자열 추가
#                 for a in alphabet:  # 알파벳들을 하나씩 제거
#                     copy = copy.replace(a, '', 1)  # 한 문자씩 제거
#                 found = True  # 숫자를 찾았으므로 found를 True로 설정
#                 break  # 다음 alphabet으로 넘어가게 break
                
#         if not found:  # 더 이상 숫자를 찾지 못했으면 루프를 종료
#             break

#     answer.append(including_nums)

# print(answer)

# numsArr = []
# for alphabet in alphabet_arr:
#   for value in arr: 
#     substring = value
#     for a in alphabet:
      
#       substring = substring.replace(a, '', 1)
#       print(substring)
    # if subString == '':
    #   numsArr.append(value)


    # if copy == '':
    #   numsArr.append(value)

# answer = []
# for i, value in enumerate(arr):
#   for strNum in alphabet_arr:
#     numArr = []
#     if all(s in value for s in strNum):
#       numArr.append(strNum)

#     value.replace(numArr[0], '')

#       # numArr.append(strNum)

#   for value in numArr:
#     print(value)
#     # answer.append(alphabet_num_dict[value])

# 딕셔너리 만들어서
# 알파벳 각각 몇개나왔는지 가운트
# 그걸로 조합해서 숫자 찾아내기
# for string in arr:
#   alphabet_dict = {}
#   for s in string:
#     if s in alphabet_dict:
#       alphabet_dict[s] += 1
#     else: 
#       alphabet_dict[s] = 1
      
#   print(alphabet_dict)

#   numArr = []
#   for nums in alphabet_arr:
#     count = 0
#     for s in nums:
#       if s in alphabet_dict:
#         count += 1
    
    
#     # 딕셔터리안에 있는 nums
#     if count == len(nums):
#       numArr.append(nums)

#   print(numArr)




# answer = []
# for value in numArr:
#   answer.append(alphabet_num_dict[value])
# answer.sort()

# print(answer)
# print("".join(map(str, answer)))