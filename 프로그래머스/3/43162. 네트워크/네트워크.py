def solution(n, computers):
    
    # 방문 여부 준비
    visited = [False] * n
    
    # 재귀로 모든 인덱스 방문하기
    def dfs(idx):
        visited[idx] = True
        
        # 방문 안한 곳 방문
        for i in range(n):
            
            # 이웃 네트워크 연결 + 방문 x
            if computers[idx][i] == 1 and not visited[i]:
                
                # 방문한 곳 재귀 실행
                dfs(i)
    
    answer = 0
    
    # 방문 안한 인덱스 찾기
    for i in range(n):
        
        # 방문 안한곳 dfs
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer