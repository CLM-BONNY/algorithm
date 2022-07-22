from collections import deque
import sys
N = int(sys.stdin.readline())

deque = deque()
for _ in range(N):
    S = sys.stdin.readline().split()
    order = S[0]
    if order == "push_front":
        deque.appendleft(S[1])
    elif order == "push_back":
        deque.append(S[1])
    elif order == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif order == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])