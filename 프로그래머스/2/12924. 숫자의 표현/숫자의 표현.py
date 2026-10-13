def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        now = 0
        cnt = 0
    # 연속된 수를 더하다가 n이상이 될때
        for j in range(i, n + 1):
        
            now = now + j
            cnt = cnt + 1
            
            if now == n:
                answer = answer + 1
            
            if now > n:
                
                # 연속된 수가 n을 넘으면 끝하고 +1
                if cnt == 2:
                    return answer + 1
                
                break
            
    return answer
    
    