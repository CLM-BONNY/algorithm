def solution(num_list):
    answer = 0
    
    sum_odd = sum(num_list[::2])
    sum_even = sum(num_list[1::2])
    
    answer = sum_odd if sum_odd >= sum_even else sum_even
    return answer