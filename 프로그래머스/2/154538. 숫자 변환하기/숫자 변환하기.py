def solution(x, y, n):
    answer = 0
    
    dp = [1000001] * (y + 1)
    dp[y] = 0
    
    for i in range(y, x - 1, -1):
        
        if dp[i] == 1000001:
            continue
            
        # 연산 종류 +n or x2 or x3
        if i - n >= x:
            dp[i - n] = min(dp[i - n], dp[i] +1)
        if i % 2 == 0 and i // 2 >= x:
            dp[i // 2] = min(dp[i // 2], dp[i] +1)
        if i % 3 == 0 and i // 3 >= x:
            dp[i // 3] = min(dp[i // 3], dp[i] +1)
    
    if dp[x] == 1000001:
        return -1
    else:
        return dp[x]