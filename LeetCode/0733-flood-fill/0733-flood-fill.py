from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # 시작 픽셀에서 시작 색을 color
        # 시작과 같은 색상을 공유하는 픽셀에 대해 직접 인접한 픽셀 칠하기
        # 업데이트 된 픽셀의 이웃도 색상과 일치할떄 색 수정
        # 마지막까지 하고 끝
        
        # BFS 문제
        
        # 상하 좌우

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        # 시작 점 큐 넣기
        q = deque()
        q.append((sr, sc))
        
        # 비교할 숫자 저장
        num = image[sr][sc]

        # 시작 좌표 색 변경
        image[sr][sc] = color

        if num == color:
            return image

        # while 
        while q:
        
            x, y = q.popleft()

            # 좌표 범위 안에 있는지
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == num:
                
                    # 큐에 넣기
                    q.append((nx, ny))

                    # image color로 색 업데이트
                    image[nx][ny] = color


        return image

