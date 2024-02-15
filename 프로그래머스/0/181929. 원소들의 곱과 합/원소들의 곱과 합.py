def solution(num_list):
    answer = 0
    num_sum, num_mul = num_list[0], num_list[0]
    
    for i in range(1, len(num_list)):
        num_sum += num_list[i]
        num_mul *= num_list[i]
        
    answer = 1 if num_mul < num_sum ** 2 else 0
    
    return answer