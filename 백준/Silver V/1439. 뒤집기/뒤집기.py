s = input()

last = -1
ones = 0
zeros = 0

for x in s:
  if x != last:
    if x == '1':
      ones += 1
    else:
      zeros += 1
    last = x

print(min(ones, zeros))