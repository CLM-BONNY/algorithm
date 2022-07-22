N = int(input())

for i in range(N):
    result = list(input())

    score, answer = 0, 0

    for x in result:
        if x == 'O':
            score += 1
            answer += score
        else:
            score = 0

    print(answer)