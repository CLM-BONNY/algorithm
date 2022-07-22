numbers = [int(input()) for i in range(9)]

idx, largest = 0, 0
for j in range(9):
    if largest < numbers[j]:
        largest = numbers[j]
        idx = j+1

print(largest)
print(idx)