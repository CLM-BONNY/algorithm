def solution(numbers, target):
    leaves = [0]
    answer = 0
    
    for n in numbers:
        tmp = []
        
        for leaf in leaves:
            tmp.append(leaf + n)
            tmp.append(leaf - n)
        
        leaves = tmp
    
    for x in leaves:
        if x == target:
            answer += 1
            
    return answer