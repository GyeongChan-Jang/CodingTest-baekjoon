TC = int(input())

for _ in range(TC):
    number = int(input())

    for i in range(2, 1_000_001):
        if i % 1_000_000 == 0:
            print('NO')
            break
        else:
            print('YES')
