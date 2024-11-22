import sys
input = sys.stdin.readline

N = int(input())
arr = [input().strip() for i in range(N)]
alphabet_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}


# 딕셔너리 만들어서
# 알파벳 각각 몇개나왔는지 가운트
# 그걸로 조합해서 숫자 찾아내기

num_alphabets = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']



# 문자열 배열 arr에 대해 반복
alphabet_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

for string in arr:
    for s in string:
        if alphabet_dict[s] == 0:  
          continue
        alphabet_dict[s] += 1 

print(alphabet_dict)
# ONE: 1
# TWO: 2
# THREE: 3
# FOUR: 4
# FIVE: 5
# SIX: 6
# SEVEN: 7
# EIGHT: 8
# NINE: 9