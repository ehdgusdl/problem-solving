# N개의 스테이지 1 ~ n 순서대로 해결 (각 스테이지 문제 푸는 비용)
# 힌트권 1 ~ n번까지 번호, i번 힌트는 i 스테이지에서만 사용
# 하나의 스테이지에서는 힌트권 최대 n-1개, 초기 힌트권 X
# 마지막을 제외한 스테이지에서 힌트 번들을 최대 1번 구매, 스테이지 별 비용 다름
# 힌트 번들에 힌트는 k장 i번 스테이지에서는 i+1 이상 번호의 힌트를 가짐
# 모든 스테이지를 해결하는데 필요한 최소 비용


# 통과 비용[1스테이즈 힌트 0개 ~ n-1개 사용 비용], 힌트[힌트 비용, 사용가능한 힌트 스테이지 종류]
def solution(cost, hint):

    n = len(cost)
    
    dp = {tuple([0] * n): 0}
    
    # 스테이지 진행 for문
    for stage in range(n):
        
        # 임시 딕셔너리 
        next_dp = {}
        
        # 현재까지 힌트 조합 for문
        for counts, current_cost in dp.items():
        
            # 현자 사용가능한 힌트 (최대 n-1)
            c = min(counts[stage], n-1)
            
            # 누적 비용
            stage_cost = current_cost + cost[stage][c]
            
            # 번들 구매 X + 힌트 고려 비용
            next_dp[counts] = min(next_dp.get(counts, float('inf')), stage_cost)
            
            # 번들 구매 (마지막 스테이지 제외)
            if stage < n - 1:
                updated_counts = list(counts)
                
                # 힌트 수량 증가
                for h in hint[stage][1:]:
                    updated_counts[h-1] = updated_counts[h-1] + 1
                # 딕셔너리 키 사용 (불변 객체만 사용 가능)
                updated_tuple = tuple(updated_counts)
                
                # 힌트 구매 비용 추가
                bundle_cost = stage_cost + hint[stage][0]
                
                # 힌트 추가 구매 비용 or 현재 비용
                next_dp[updated_tuple] = min(next_dp.get(updated_tuple, float('inf')), bundle_cost)
        
        # 마지막 dp 갱신
        dp = next_dp
    
    # 최솟값 리턴
    return min(dp.values())