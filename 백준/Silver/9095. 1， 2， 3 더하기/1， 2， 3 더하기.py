def go(sum, goal) :
    if (sum > goal) :
        return 0
    if (sum == goal) :
        return 1
    now = 0
    for i in range(1,4) :
        now += go(sum+i, goal)
    return now;

n = int(input())
for _ in range(n) :
    print(go(0, int(input())))