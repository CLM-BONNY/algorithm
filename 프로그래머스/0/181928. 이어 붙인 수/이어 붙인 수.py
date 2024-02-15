def solution(num_list):
    answer = 0
    num_odd, num_even = "", ""
    
    for x in num_list:
        if x % 2 == 1:
            num_odd += str(x)
        else:
            num_even += str(x)
    
    answer = int(num_odd) + int(num_even)
    
    return answer