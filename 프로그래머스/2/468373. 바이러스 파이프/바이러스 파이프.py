# 1 ~ n까지 n개 배양체 n-1개 파이프 # 트리 모양
# 파이프 A, B, C 3개 종류
# 열림 파이프로 인접 배양체 감영
# 종류가 같은 파이프를 한번에 모두 열었다 닫을 수 있음 + 닫기전에 다른걸 열 수 없음 (K번 동안)

from collections import deque

# 배양체 개수 # 초기 감염 번호 # 노드 정보(x번 노드, y노드(x < y), 파이프 종류) # 행동 수
def solution(n, infection, edges, k):
    
    answer = 0
        
    # BFS
    # 큐 (현재 노드 + 감염 노드 + 횟수)
    q = deque()
    
    # 초기 큐 설정 # 빈 셋 # 0  
    q.append([{infection} , 0])
    
    # while (큐에 있는 걸 다 쓸때까지)
    while q:
        
        virus, cnt = q.popleft()
        
        # k번 전에 전부 감염 가능
        answer = max(answer, len(virus))
        
        # k == 횟수면 끝
        if k == cnt:
            continue
        
        # A, B, C 감염 상태
        A = set(virus)
        B = set(virus)
        C = set(virus)
        
        # for문으로 다음에 열 파이프
        for _ in range(n):
            
            # 감염 노드 기준 갈수있는 노드 확인 + # A or B or C 나눠서 고려
            for node1, node2, pipe in edges:
                
                # 연결 여부 확인 
                # pipe가 1 or 2 or 3 + 연쇄 확장 고려
                if pipe == 1 and (node1 in A or node2 in A):
                    A.add(node1)
                    A.add(node2)

                if pipe == 2 and (node1 in B or node2 in B):
                    B.add(node1)
                    B.add(node2)

                if pipe == 3 and (node1 in C or node2 in C):
                    C.add(node1)
                    C.add(node2)
            
        # 모든 감염 큐에 삽입
        q.append([A, cnt + 1])
        q.append([B, cnt + 1])
        q.append([C, cnt + 1])
            
        
    return answer