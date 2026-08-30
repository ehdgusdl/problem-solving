def solution(N, number):
    if N == number:
        return 1
    
    # set 만들기 중복 방지
    dp = [set() for _ in range (9)]
    
    #N을 i번 연속 사용하는 숫자 추가 (5, 55, 555)
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        
        # 다음단계 사칙 연산 계산
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)

                    if op2 !=0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
        
    #8번 안에 없을때
    return -1
    
    
    
    