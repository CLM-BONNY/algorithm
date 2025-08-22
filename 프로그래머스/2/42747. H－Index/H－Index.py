def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i, v in enumerate(citations):
        if v >= i+1:
            answer = i+1
        else:
            break

    return answer