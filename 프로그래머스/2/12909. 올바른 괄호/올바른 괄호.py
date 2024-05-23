def solution(s):
    answer = True
    
    stack = []
    
    for item in s:
        if item == "(":
            stack.append(item)
        elif len(stack) != 0:
            stack.pop()
        elif len(stack) == 0:
            return False
        
    if len(stack) != 0:
        answer = False
    
    return answer