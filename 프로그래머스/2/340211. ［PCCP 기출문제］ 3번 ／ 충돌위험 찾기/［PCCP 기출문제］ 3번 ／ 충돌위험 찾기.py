# 2차원 좌표, n개의 포인트가 존재 1~ n개
# 운송 경로 m개 포인트로 구성 할당된 포인트를 순서대로 방문
# 로봇 x대, 0초 동시 출발한다
# 1초마다 r좌표 c좌표 중 1만큼 이동 둘다 최단 경로로 이동하고 두가지일 경우 r부터
# 좌표에 로봇 2대 이상이면 충돌 가능성 있음
# n개의 좌표를 담은 2차 배열 points와 로봇 x대의 운송 경로
# 위험한 상황의 수를 리턴

def solution(points, routes):
    
    robot_paths = []
    
    
    # 모든 로봇의 경로를 하나씩 처리
    for route in routes:
        path = []
        
        # 시작 위치
        cur_r, cur_c = points[route[0] -1]
        path.append((cur_r, cur_c))
        
        # 다음 목적지 어디인지
        for next_point in route[1:]:
            
            target_r, target_c = points[next_point -1]
            
            # 세로 부터 이동
            while cur_r != target_r:
                
                if cur_r < target_r:
                    cur_r = cur_r + 1
                
                else:
                    cur_r = cur_r - 1
                    
                path.append((cur_r, cur_c))

            
            # 가로 이동하기
            while cur_c != target_c:
                
                if cur_c < target_c:
                    cur_c = cur_c + 1
                else:
                    cur_c = cur_c -1
                    
                path.append((cur_r, cur_c))
    
        robot_paths.append(path)
    
    # 딕셔너리로 같은 시간 같은 좌표를 키로 두고 비교
    loc_count = {}
    
    # 진행시 같은 칸에 두개이상 있는지?
    for path in robot_paths:
        for t, loc in enumerate(path):
            key = (t, loc)
            loc_count[key] = loc_count.get(key, 0) + 1
    
    answer = 0
    
    for count in loc_count.values():
        if count >= 2:
            answer += 1
    
    
    return answer