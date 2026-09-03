from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    # 1. 시작 지점 레버까지 거리
    # 2. 레버에서 출구까지
    
    # BFS 문제
    # 시작, 레버, 출구 찾기
    start = []
    mid = []
    end = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                mid = [i, j]
            elif maps[i][j] == 'E':
                end = [i, j]
    
    ## 상하 좌우

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]



    # while
    def bfs(sx, sy, ex, ey):

        visited = [[0]*m for _ in range(n)]

        # 시작 점 큐 넣기
        q = deque()
        q.append((sx, sy))


        while q:

            x, y = q.popleft()

            if x == ex and y == ey:
                return visited[x][y]

            # 좌표 범위 안에 있는지
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m: 
                    if maps[nx][ny] != 'X' and not (nx == sx and ny == sy):

                        # 큐에 넣기
                        if visited[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = visited[x][y] + 1


        return -1

    ans1 = bfs(start[0], start[1], mid[0], mid[1])
    ans2 = bfs(mid[0], mid[1], end[0], end[1])
    
    if ans1 == -1 or ans2 == -1:
        return -1
    
    return ans1 + ans2 