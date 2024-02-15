str = input()

for x in str:
    x = x.lower() if x.isupper() else x.upper()
    print(x, end="")