import sys
input = sys.stdin.readline

number = input().strip()

numbers = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '-1',
    '4': '-1',
    '5': '5',
    '6': '9',
    '7': '-1',
    '8': '8',
    '9': '6'
}

def isPrime(number):
    cnt = 0
    for i in range(2, number + 1):
        if i * i > number:
            break

        if number % i == 0:
            cnt += 1
    if cnt == 0:
        return True
    else:
        return False


# 주어진 수와 뒤집힌 수가 소수인지 판단

# 뒤집힌 수 구하기: 인덱스 이용해 뒤집고 변환
reversed_number = ''
for i in range(len(number) -1, -1, -1):
    if numbers[number[i]] == '-1':
        break
    else:
        reversed_number += numbers[number[i]]

if reversed_number == '':
    print('no', end=" ")
elif len(reversed_number) != len(number):
    print('no', end=" ")
elif isPrime(int(number)) and isPrime(int(reversed_number)):
    print('yes', end=" ")
else:
    print('no', end=" ")
