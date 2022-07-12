import math

N = int(input())
num = list(map(int, input().split()))

cnt = 0
for i in num:
    flag = "false"
    if i > 1:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = "true"
                break
        if flag == "false":
            cnt += 1
            
print(cnt)