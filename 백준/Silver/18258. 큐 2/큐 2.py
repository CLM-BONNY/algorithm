from collections import deque
import sys
N = int(sys.stdin.readline())

queue = deque()
for i in range(N):
    s = sys.stdin.readline().split()
    order = s[0]
    if order == "push":
        queue.append(s[1])
    elif order == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])