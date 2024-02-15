def solution(binomial):
    answer = 0
    binomial_split = binomial.split()
    
    if binomial_split[1] == "+":
        answer = int(binomial_split[0]) + int(binomial_split[2])
    elif binomial_split[1] == "-":
        answer = int(binomial_split[0]) - int(binomial_split[2])
    else:
        answer = int(binomial_split[0]) * int(binomial_split[2])
    
    return answer