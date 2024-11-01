import sys

def round_half_up(number):  # 사사오입 반올림 함수 정의
    return int(number) + (1 if number - int(number) >= 0.5 else 0)

# 입력 받기
total_count = int(sys.stdin.readline())
excluded_count = round_half_up(total_count * 0.15)  # 상위와 하위에서 제외할 인원 수 계산

if total_count == 0:
    print(0)
else:
    # 입력을 한 번에 읽고, 공백을 기준으로 분리하여 리스트로 변환
    scores = list(map(int, sys.stdin.read().split()))
    
    scores.sort()  # 점수 리스트를 오름차순으로 정렬
    
    # 결과 합산
    result_sum = 0
    for i in range(excluded_count, total_count - excluded_count):
        result_sum += scores[i]  # 제외할 인원을 제외한 점수들만 합산
    
    # 평균 계산 및 출력
    result_average = result_sum / (total_count - 2 * excluded_count)
    print(round_half_up(result_average))
