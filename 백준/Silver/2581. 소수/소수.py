import math

M = int(input())
N = int(input())

answer = []
for i in range(M, N+1):
    flag = "false"
    if i > 1:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = "true"
                break
        if flag == "false":
            answer.append(i)

if len(answer) > 0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)