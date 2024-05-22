def solution(progresses, speeds):
    # 완료까지 남은 일수 계산
    days_left = [(100 - progresses[i] + speeds[i] - 1) // speeds[i] for i in range(len(progresses))]
    
    answer = []
    current_release_day = days_left[0]  # 현재 배포일 설정 (첫 기능의 완료일)
    count = 0  # 배포할 기능의 수
    
    for day in days_left:
        if day > current_release_day:
            # 현재 날짜보다 더 늦게 완성되는 기능이면, 지금까지 쌓인 기능 배포
            answer.append(count)
            current_release_day = day  # 배포일 갱신
            count = 1  # 새 배포 사이클 시작
        else:
            # 같은 날짜에 배포 가능하면 기능 수 증가
            count += 1
    
    # 마지막으로 쌓인 기능 배포
    answer.append(count)
    
    return answer