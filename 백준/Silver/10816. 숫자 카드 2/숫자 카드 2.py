from collections import Counter

# 입력 받기
N = int(input().strip())
cards = list(map(int, input().strip().split()))
M = int(input().strip())
targets = list(map(int, input().strip().split()))

# 카드 빈도 계산
card_count = Counter(cards)

# 결과 생성
result = [card_count[target] for target in targets]

# 결과 출력하기
print(' '.join(map(str, result)))
