# 루트 노드, 리프 노드, 분배 노드
# 루트는 자식 1개 분배 자식 2 or 3개 리프 자식 X
# 같은 깊이의 분배 노드의 자식 수는 모두 같아야 함
# 분배도는 split_limit 작거나 같아야 함 # 루트 까지의 최단 경로를 이루는 노드의 자식 수의 곱
# 분배 노드는 최대 개수 dist_limit
# 리프노드 수 리턴

def solution(dist_limit, split_limit):
    
    answer = 1 # 분배 노드 0개여도 리프 1개
    
    # 위에서 아래로 내려가면서 2 or 3 분배 노드 
    # 2를 a번 + 3을 b번 사용
    
    a = 0
    # 조건: 2^a * 3^0 <= split_limit
    while 2 ** a <= split_limit:
        b = 0
        
        # 조건: 2^a * 3^b <= split_limit
        while 2 ** a * 3 ** b <= split_limit:
    
            # 레벨마다 확장할 수 있는 만큼 확장: min(현재 노드 수, 남은 예산)
            # 확장 1번당 리프 +(자식 수-1), 다음 레벨 노드 수 = 확장 수 * 자식 수
            
            # 남은 분배 노드 예산, 맨 아래 리프 수, 모든 리프 수
            remain_dist, nodes, leaves = dist_limit, 1, 1

            # 레벨마다 자식 수를 하나씩 꺼냄 (2 먼저, 3 나중)
            for child in [2] * a + [3] * b:
                
                # 예산을 다 쓰면 더 못 내려감
                if remain_dist == 0:
                    break
                
                # 바꿀 수 있는 기회 (맨 아래 피프 수와 예산 중 작은 쪽)
                k = min(nodes, remain_dist)
                
                # 쓴 만큼 예산 차감
                remain_dist = remain_dist - k
                
                # 1개 바꿀 때마다 리프 1개 사라지고 child개 생김 +(child - 1)
                leaves = leaves + k * (child - 1)
                
                # 바꾼 노드들의 자식이 다음 레벨 노드가 됨
                nodes = k * child
    
            # 모든 (a, b) 중 리프 수 최댓값
            answer = max(answer, leaves)
            b = b + 1
            
        a = a + 1
    
    return answer