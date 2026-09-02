def solution(m, n, puddles):
    
    # dp 세팅
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # 물웅덩이 셋
    puddle_set = {(y, x) for x, y in puddles}
    
    # 시작 지점
    dp[1][1] = 1
    
    # 바텀 업
    for x in range(1, n+1):
        for y in range(1, m+1):
            
            if x == 1 and y == 1:
                continue
            
            # 물웅덩이 피하기
            if (x, y) in puddle_set:
                dp[x][y] = 0
                
            else:
                # 이전 경우의 수 더하기
                dp[x][y] = dp[x][y-1] + dp[x-1][y]
    
    return dp[n][m] % 1000000007