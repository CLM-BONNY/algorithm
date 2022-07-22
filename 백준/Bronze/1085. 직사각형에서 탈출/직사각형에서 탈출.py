x, y, w, h = map(int, input().split())

d = min(x, w-x, h-y, y)

print(d)