def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return int((a * b) / gcd(a, b))


T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    if a < b:
        tmp = a
        a = b
        b = tmp
    print(lcm(a, b))
