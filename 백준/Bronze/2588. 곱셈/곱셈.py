a = int(input())
b = input()
c = [int(x) for x in b]
for i in range(len(c)-1,-1,-1):
    print(a*c[i])
print(a*int(b))