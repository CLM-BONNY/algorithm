T = int(input())

for x in range(T):
    R, S = input().split()
    R = int(R)
    for y in S:
        for j in range(R):
            print(y, end="")
    print()