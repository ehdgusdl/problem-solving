# N개의 퍼즐 각 퍼즐은 난이도와 소요 시간 정해져있음
# 숙련도에 따라 틀리는 횟수 # 소요시간 cur를 사용 
# 난이도 - 레벨 횟수 만큼 틀림 * ( time_cur + time_prev ) + time_cur
# 제한 시간안의 숙련도 구하기

# 난이도 # 현재 소요 시간 # 이전 퍼즐 소요시간 # 숙련도
def solution(diffs, times, limit):
    
    left = 1
    right = max(diffs)
    answer = right
    
    # 숙련도를 바꾸면서 반복하기
    while left <= right:
        skill = (left + right) // 2
        total_time = 0
        
        # 인덱스 기준으로 실험
        for idx in range(len(diffs)):
            
            time_cur = times[idx]
            time_prev = 0
            
            if idx > 0:
                time_prev = times[idx-1]

            # 숙련도가 낮을떄
            if diffs[idx] > skill:
                total_time = total_time + (time_cur + time_prev) * (diffs[idx] - skill) + time_cur

            # 숙련도가 높거나 같을때
            else:
                total_time = total_time + time_cur 
            
            # 제한 시간이 넘으면 루프 탈출
            if total_time > limit:
                break
        
        # 토탈 시간 안 넘었으면 숙련도 낮추기
        if total_time <= limit:
                answer = skill
                right = skill -1
        
        # 토탈 시간 넘으면 숙련도 높이기
        else:
            left = skill + 1
    
    return answer
    
