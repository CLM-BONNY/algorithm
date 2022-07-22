import math

numbers = list(map(int, input().split()))

answer = 0
for i in numbers:
    answer += math.pow(i, 2)

print(int(answer%10))