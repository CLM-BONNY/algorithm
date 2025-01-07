from itertools import permutations

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 입력된 숫자 정렬
numbers.sort()

# 중복 제거를 위해 set 사용
result = set(permutations(numbers, M))

# 결과를 사전 순으로 출력
for seq in sorted(result):
    print(' '.join(map(str, seq)))
