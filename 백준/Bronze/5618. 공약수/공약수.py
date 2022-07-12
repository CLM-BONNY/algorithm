import sys


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

g = gcd(num[0], gcd(num[1], num[-1]))

for i in range(1, g // 2 + 1):
    if g % i == 0:
        print(i)
print(g)