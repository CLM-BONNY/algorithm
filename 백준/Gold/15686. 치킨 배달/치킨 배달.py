import sys
from itertools import combinations

def get_chicken_distance(houses, chicken_shops):
    total_distance = 0

    for hx, hy in houses:
        min_dist = float('inf')
        for cx, cy in chicken_shops:
            min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
        total_distance += min_dist

    return total_distance

def solve(N, M, city):
    houses = []
    chicken_shops = []

    # 도시 정보 파싱
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chicken_shops.append((r, c))

    # 치킨집 조합 중 최소 거리 찾기
    min_chicken_distance = float('inf')

    for selected_chickens in combinations(chicken_shops, M):
        min_chicken_distance = min(min_chicken_distance, get_chicken_distance(houses, selected_chickens))

    return min_chicken_distance

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과 출력하기
print(solve(N, M, city))
