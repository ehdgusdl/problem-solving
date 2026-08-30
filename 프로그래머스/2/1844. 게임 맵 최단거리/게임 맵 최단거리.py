from collections import deque
def solution(maps):
    
    # 그래프 크기
    n = len(maps)
    m = len(maps[0])
    
    # 이동 할수 있는 경우의 수
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 큐에 만들기 (시작 지점 0, 0)
    q = deque([[0, 0]]) 
    
    # 큐에 하나씩 수를 꺼내서 실행 (while)
    while q:
        x, y = q.popleft()
        
        # 상하 좌우 하나씩 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 할수 있으면 큐에 넣기(범위) + 아직 안가본곳 = 1
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:

                # 이동 할때 마다 동선에 + 1 하기
                maps[nx][ny] = maps[x][y] + 1

                # 다음 동선 큐에 넣기
                q.append([nx, ny])
    
    # while 끝나고 마지막에 n, m 값을 리턴
    if maps[n-1][m-1] == 1:
        return -1
    else: 
        return maps[n-1][m-1]