import sys

# 입력 받기
M = int(sys.stdin.readline())

# 공집합 S
S = set()

for i in range(M):
  command = sys.stdin.readline().strip().split()
  
  if len(command) == 2:
    a, b = command[0], int(command[1])
    
    if a == "add":
      S.add(b)
    elif a == "remove":
      S.discard(b)
    elif a == "check":
      print(1 if b in S else 0)
    elif a == "toggle":
      if b in S:
        S.remove(b)
      else:
        S.add(b)
    
  else:
    a = command[0]
    
    if a == "all":
      S = set(range(1, 21))
    elif a == "empty":
      S.clear()