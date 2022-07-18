inp = []
stack = []
cnt = 0
answer = 0

inp = list(input())

for i in inp:
    if i == '(':
        stack.append(i)
        cnt = 0
    elif i == ')':
        stack.pop()
        if cnt == 0:
            if len(stack) > 0:
                answer += len(stack)
        else:
            answer += 1
        cnt = 1

print(answer)