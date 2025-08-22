
def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    for item, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = [item]
        else:
            clothes_dict[category].append(item)
    
    for items in clothes_dict.values():
        answer *= len(items) + 1

    return answer - 1