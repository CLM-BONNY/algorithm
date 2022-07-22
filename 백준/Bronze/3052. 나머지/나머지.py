remainder = []
for i in range(10):
    remainder.append(int(input())%42)

answer = set(remainder)

print(len(answer))