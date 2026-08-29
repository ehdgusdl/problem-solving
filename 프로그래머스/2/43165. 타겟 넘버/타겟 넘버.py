def solution(numbers, target):
    answer = [0]
    
    # 재귀적으로 풀기
    def dfs(cnt, num):
        
        # 재귀 시작시 재귀 수 비교
        if len(numbers) == cnt:
            
            # 타겟과 현재 수 비교 후 +1 하기
            if num == target:
                answer[0] = answer[0] + 1

        # 다음 재귀 더하기 or 빼기
        if len(numbers) > cnt:
            dfs(cnt+1, num + numbers[cnt])
            dfs(cnt+1, num - numbers[cnt])
        
    dfs(0, 0)
    return answer[0]