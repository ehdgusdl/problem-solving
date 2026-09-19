# 항상 초록불 → 노란불 → 빨간불 순서 but 지속시간 다름
# 처음은 초록불 상태로 시간은 1초 부터
# 전부 노랭이면 정전
# 가장 빠른 정전 시간 or 없으면 -1

import math

def solution(signals):
    
    cnt = 0
    
    # 존재하지 않는 경우 어떻게 아는지? -> 최소 공배수 횟수 까지   
    # 최소 공배수 math.lcm
    lcm_num = math.lcm(*[sum(s) for s in signals])
    
    # 최소 공배수 이전엔 끝나야 함
    for i in range(1, lcm_num+1):
        
        color_y = True
        
        # 현재 어느 신호인지
        for sig in signals:
            idx = i % sum(sig)
            
            # 노랭이 확인하기
            if not (sig[0] < idx <= sig[0] + sig[1]):
                color_y = False
                break
        
        # 모든 색 노랭이
        if color_y == True:
            return i
        
    return -1