# 문제 4. 숫자야구 ( # 2503 )

# A는 3자리 숫자로 된 정답을 하나 정합니다.

# B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 합니다.

# B가 말한 숫자가 정답에 포함되어 있다면 1 Ball입니다.
# B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1 Strike입니다.

# 다른 숫자로 이루어진 세 자리수

# Strike와 Ball의 결과를 보고, 가능한 숫자를 계산하는 프로그램을 작성하세요.

# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1

# 2

n = int(input())
hint = [list(map(str, input().split())) for _ in range(n)]
answer = 0

# 세자리 숫자 탐색
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            # 숫자 정해졌다면 hint에 부합한지 check

            # 서로 다른 숫자로 구성됨
            if a == b or a == c or b == c:
                continue

            count = 0
            for [number, strike, ball] in hint:
                # 직접 스트라이크, 볼 카운트 세기
                
                strike = int(strike)
                ball = int(ball)
                
                ball_count = 0
                strike_count = 0
            
                # 스트라이크 계산기
                if a == int(number[0]):
                    strike_count += 1
                if b == int(number[1]):
                    strike_count += 1
                if c == int(number[2]):
                    strike_count += 1

                # 볼 계산기
                if a == int(number[1]) or a == int(number[2]):
                    ball_count += 1 
                if b == int(number[0]) or b == int(number[2]):
                    ball_count += 1
                if c == int(number[0]) or c == int(number[1]):
                    ball_count += 1
                
                # 현재 검사하고 있는 숫자가 힌트의 조건에 맞으면 count 증가
                if ball_count == ball and strike_count == strike:
                    count += 1

            # 현재 검사하고 있는 숫자가 힌트의 모든 조건을 만족하므로 A가 생각하는 답일 수 있음!
            if count == n:
                answer += 1
print(answer)