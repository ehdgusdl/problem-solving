def solution(sequence):
    
    answer = 0
    
    plus = [-1, 1]
    minus = [1, -1]
    
    now1 = 0
    now2 = 0
    # for 문으로 모든 인덱스 돌기
    # [1, -1] or [-1, 1] 끝까지 하기
    # max로 제일 큰거 기록해두기
    for i in range(len(sequence)):
        now1 = max(now1, 0) + sequence[i] * plus[i % 2]
        now2 = max(now2, 0) + sequence[i] * minus[i % 2]
        answer = max(answer, now1, now2)
        
             
        
    return answer