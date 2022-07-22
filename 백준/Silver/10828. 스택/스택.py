import sys

numstack = []
length = int(sys.stdin.readline())
for i in range(length):
    stc = sys.stdin.readline().split()
    order = stc[0]
    if "push" == order:
        numstack.append(stc[1])
    elif "pop" == order:
        if len(numstack) == 0:
            print(-1)
        else:
            print(numstack.pop())
    elif "size" == order:
        print(len(numstack))
    elif "empty" == order:
        if len(numstack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(numstack) == 0:
            print(-1)
        else:
            print(numstack[-1])