def solution(N, number):
    
    # N = num  리턴 1
    if N == number:
        return 1
    # 중복 제거 용 Set
    dp = [set() for _ in range(9)]
    
    # N을 i번 써서 만들수 있는 모든 경우의 수
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        
        for j in range(1, i):

            # 최대 i번 계산
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    
                    # 사칙연산 한번씩
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    
                    # 나누기 조건
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        # i번 했을때 만들어 졌는지 확인
        if number in dp[i]:
            return i
        
    # 8번 안에 안되면 -1
    return -1
    
    
    
    