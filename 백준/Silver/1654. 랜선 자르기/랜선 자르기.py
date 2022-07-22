def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())

line = []
res, largest = 0, 0

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lower = 1
upper = largest

while lower <= upper:
    middle = (lower+upper)//2

    if Count(middle) >= n:
        res = middle
        lower = middle+1
    
    else:
        upper = middle-1

print(res)