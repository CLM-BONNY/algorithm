from itertools import combinations

# 입력 받기
n, m = map(int, input().split())

# 1부터 N까지의 수 중에서 M개를 고르는 조합 생성
for comb in combinations(range(1, n + 1), m):
    print(' '.join(map(str, comb)))
