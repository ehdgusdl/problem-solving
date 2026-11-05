# N X M 격자 모양
# 빨간색 파란색 수례 하나씩 시작 -> 도착 이동하면 끝
# 각 턴마다 상하좌우로 이동 
# 왔던곳 X 도착하면 끝 동시에 같은 칸 X 수례끼리 자리 바꾸기 X
# 이동 횟수 최솟 값 구하기 못하면 0

# 0 빈칸 1, 3 빨갱이 시작과 끝 2, 4 파랭이 시작과 끝 벽 5

import sys

# 백트래킹 재귀 깊이 해제
sys.setrecursionlimit(10**6)

def solution(maze):
    
    answer = 0
    
    n = len(maze)
    m = len(maze[0])
    
    # 방문 여부 리스트
    r_visited = [[0]* m for _ in range(n)]
    b_visited = [[0]* m for _ in range(n)]
    
    # 상하좌우 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 시작 지점 끝 지점 정의하기
    for a in range(n):
        for b in range(m):
            if maze[a][b] == 1:
                r_start = [a, b]
                r_visited[a][b] = 1
                
            if maze[a][b] == 2:
                b_start = [a, b]
                b_visited[a][b] = 1
            
            if maze[a][b] == 3:
                r_end = [a, b]
                
            if maze[a][b] == 4:
                b_end = [a, b]

    
    min_cnt = [float('inf')]
    
    def dfs(rx, ry, bx, by, cnt):
        
        # 기존 횟수보다 높아지면 재귀 X
        if cnt > min_cnt[0]:
            return
        
        # 두개 모두 도착 한 경우 더 적은 이동횟수 업데이트
        if r_end == [rx, ry] and b_end == [bx, by]:
            min_cnt[0] = min(min_cnt[0], cnt)
            return
        
        r_next_list = []
        
        # 도착 했으면 현재 위치 유지
        if [rx, ry] == r_end:
            r_next_list.append([rx, ry])
        else:
            # 빨갱이 이동 경우의 수
            for i in range(4):
                nrx = rx + dx[i]
                nry = ry + dy[i]
                
                if 0 <= nrx < n and 0 <= nry < m and maze[nrx][nry] != 5:
                    if r_visited[nrx][nry] == 0:
                        r_next_list.append([nrx, nry])
        
        b_next_list = []
        
        # 도착 했으면 현재 위치 유지
        if [bx, by] == b_end:
            b_next_list.append([bx, by])
        else:
            # 파랭이 이동 경우의 수
            for i in range(4):
                nbx = bx + dx[i]
                nby = by + dy[i]
                
                if 0 <= nbx < n and 0 <= nby < m and maze[nbx][nby] != 5:
                    if b_visited[nbx][nby] == 0:
                        b_next_list.append([nbx, nby])
        
        # 빨갱이 파랭이 다음 경로의 모든 경우의 수
        for nrx, nry in r_next_list:
            for nbx, nby in b_next_list:
                
                # 같은 위치 X
                if [nrx, nry] == [nbx, nby]:
                    continue
                
                # 동시에 각자 자리 위치 변경 X
                if [nrx, nry] == [bx, by] and [nbx, nby] == [rx, ry]:
                    continue
                
                # 방문 처리
                r_visited[nrx][nry] = 1
                b_visited[nbx][nby] = 1
                
                # 재귀 
                dfs(nrx, nry, nbx, nby, cnt + 1)
                
                # 백트래킹 (도착하지 않았던 수레만 방문 해제)
                if [rx, ry] != r_end:
                    r_visited[nrx][nry] = 0
                    
                if [bx, by] != b_end:
                    b_visited[nbx][nby] = 0
    
    # 시작
    dfs(r_start[0], r_start[1], b_start[0], b_start[1], 0)
    
    # inf면 0 아니면 min_cnt[0]이 정답
    if min_cnt[0] == float('inf'):
        answer = 0
    else:
        answer = min_cnt[0]
    
    return answer