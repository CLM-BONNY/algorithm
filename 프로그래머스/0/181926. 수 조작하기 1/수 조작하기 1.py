def solution(n, control):
    answer = n
    
    for x in control:
        if x == "w":
            answer += 1
        elif x == "s":
            answer -= 1
        elif x == "d":
            answer += 10
        else:
            answer -= 10
    
    return answer