from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        answer = 0

        # 그래프 풀기 위해 하나씩 방문하기 0이면 안가본곳
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        # 큐 정의
        q = deque() 

        # x, y 이동 범위

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        # BFS
        # for 이용해서 모든 인덱스를 방문하는게 목표
        for i in range(m):
            for j in range(n):

            # for 하나씩 돌때마다 섬 개수 +1
                if visited[i][j] == 0 and grid[i][j] == '1':
                    visited[i][j] = 1
                    answer = answer + 1
                    q.append((i, j))

                    while q:
                        x, y = q.popleft()

                    # 상하좌우 하나씩 방문
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                q.append((nx, ny))

        
        return answer

        