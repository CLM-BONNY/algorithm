def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    
    for item, type in clothes:
        if type not in clothes_dict:
            clothes_dict[type] = [item]
        else:
            clothes_dict[type].append(item)
        
    
    for items in clothes_dict.values():
        answer *= (len(items)+1)
    
    return answer-1