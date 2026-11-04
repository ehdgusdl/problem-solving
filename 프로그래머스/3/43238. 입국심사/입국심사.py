# 심사 시간 최소로
# 기다리는 사람 N, 각 심사 걸리는 시간 times
# 모든 사람 최솟값

def solution(n, times):
    
    left = 1
    right = max(times)*n
    
    answer = right
    
    while left <= right:
        
        # 총걸린 시간
        mid = (left + right) // 2
        
        total_people = 0
        
        for t in times:
            
            # 각 심사관이 몇명씩 처리 할수 있는지
            total_people = total_people + mid // t
        
        # 여유가 남아있으면 반복
        if total_people >= n:
            answer = mid
            right = mid - 1
        
        # 처리 시간 늘리기
        else:
            left = mid + 1
            
    return answer