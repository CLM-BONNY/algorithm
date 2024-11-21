def flatten_land(n, m, b, land):
    # 높이별 블록 개수를 저장하는 딕셔너리
    height_counts = [0] * 257

    # 높이별 블록 개수 집계
    for i in range(n):
        for j in range(m):
            height_counts[land[i][j]] += 1

    # 가능한 높이를 순회하며 최소 시간 계산
    min_time = float('inf')
    best_height = 0

    # 모든 높이에 대해 시뮬레이션
    for target_height in range(257):
        remove_blocks = 0
        add_blocks = 0

        for h in range(257):
            if height_counts[h] > 0:
                if h > target_height:  # 블록 제거가 필요
                    remove_blocks += (h - target_height) * height_counts[h]
                elif h < target_height:  # 블록 추가가 필요
                    add_blocks += (target_height - h) * height_counts[h]

        # 현재 인벤토리로 가능 여부 확인
        if remove_blocks + b >= add_blocks:
            time = remove_blocks * 2 + add_blocks
            # 최소 시간으로 갱신하거나, 시간이 같다면 더 높은 땅 선택
            if time < min_time or (time == min_time and target_height > best_height):
                min_time = time
                best_height = target_height

    return min_time, best_height


# 입력 받기
n, m, b = map(int, input().split())  # 세로, 가로, 인벤토리 블록 개수
land = [list(map(int, input().split())) for _ in range(n)]  # 땅 높이 정보

# 결과 계산
time, height = flatten_land(n, m, b, land)

# 결과 출력
print(time, height)
