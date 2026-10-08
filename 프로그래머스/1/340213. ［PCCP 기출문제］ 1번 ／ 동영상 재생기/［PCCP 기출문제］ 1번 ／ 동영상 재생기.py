# 10초 전으로 이동(prev), 10초 후로 이동(next), 오프닝(op_end) 이후로 (구간안에)

# 동영상의 길이 # 직전의 재생위치 # 오프닝 시작, 끝 # 사용자 입력
def solution(video_len, pos, op_start, op_end, commands):
    


    
    # mm:ss 형식
    video_end = int(video_len[0:2]) * 60 + int(video_len[3:5])
    t_pos = int(pos[0:2]) * 60 + int(pos[3:5])
    t_ops = int(op_start[0:2]) * 60 + int(op_start[3:5])
    t_ope = int(op_end[0:2]) * 60 + int(op_end[3:5])
    

    
    for command in commands:
        
        
        # 오프닝 구간이면 스킵
        if t_ops <= t_pos and t_pos <= t_ope:
            t_pos = t_ope
        
        # next: +10 prev: -10
        if command == 'next':
            
            t_pos = t_pos + 10
            
            if video_end < t_pos:
                t_pos = video_end
            
        if command == 'prev': 
            t_pos = t_pos - 10
            
            if t_pos < 0:
                t_pos = 0
            
    # 오프닝 구간이면 스킵
    if t_ops <= t_pos and t_pos <= t_ope:
        t_pos = t_ope
    
    mm = str(t_pos // 60)
    ss = str(t_pos % 60)

    if len(mm) < 2:
        mm = '0' + mm
        
    if len(ss) < 2:
        ss = '0' + ss
    
    return mm + ':' + ss