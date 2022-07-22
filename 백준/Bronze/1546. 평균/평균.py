N = int(input())
numbers = list(map(int, input().split()))

new = 0
M = max(numbers)
for i in numbers:
    new += i/M*100

print(new/N)