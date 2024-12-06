import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

unique_arr = set(arr)
# count_arr = [0 for _ in range(len(unique_arr))]


for i in unique_arr:
    copy_arr = [x for x in arr if x != i]
    count = 0
    l = 0
    r = 1
    print(i, copy_arr)
    while l > r:
        if copy_arr[l] == copy_arr[r]:
            count += 1
            r += 1
        else:
            l += 1
            r += 1
