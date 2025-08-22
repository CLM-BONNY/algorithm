def solution(nums):
    answer = 0
    
    ponketmons = set(nums)
    
    if len(ponketmons) > (len(nums)/2):
        answer = (len(nums)/2)
    else:
        answer = len(ponketmons)

    return answer