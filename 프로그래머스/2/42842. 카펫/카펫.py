def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for w in range(total, 0, -1):
        if total % w != 0:
            continue
        
        h = total // w
        y = (w-2) * (h-2)
        b = total-y
        
        if y == yellow and b == brown:
            answer.append(w)
            answer.append(h)
            break
    
    return answer