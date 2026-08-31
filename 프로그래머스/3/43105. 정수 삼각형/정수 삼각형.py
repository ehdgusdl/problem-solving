# 바텀업으로 풀자
# 올라가면서 더하는데 기존값과 비교해서 누가 더큰지 해서 업데이트 방식으로
# 마지막에 제일큰 값 리턴

def solution(triangle):
    
    # dp n개 리스트 생성
    dp = [[0]*(n+1) for n in range(len(triangle))]
    dp[0] = triangle[0]

    # 이전 값을 사용하여 기존값과 비교 
    # row 기준 + 2번째 줄부터
    for row in range(1, len(triangle)):
        
        # column 기준
        for column in range(row + 1):
            
            # 인덱스  0일때
            if column == 0:
                dp[row][0] = dp[row -1][0] + triangle[row][0]
                continue
            
            # 마지막 인덱스 일때
            elif column == row:
                dp[row][-1] = dp[row -1][-1] + triangle[row][-1]
                continue
                
            # triangle[row][column]에 더해 비교하여 더 큰거로 업데이트
            # dp[row -1][column-1] VS dp[row][column-1]
            dp[row][column] = triangle[row][column] + max(dp[row -1][column -1], dp[row-1][column])
        
    # 마지막 리스트에서 제일큰값 리턴
    
    return max(dp[-1])