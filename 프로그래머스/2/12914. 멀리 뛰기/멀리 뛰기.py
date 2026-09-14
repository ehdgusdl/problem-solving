def solution(n):
    
    answer = [0, 1, 2]
    # answer[1] = 1 and answer[2] = 2
    
    if n <= 2:
        return answer[n]
    
    # 점프 1 or 2칸
    # answer[n] = answer[n-1] + answer[n-2]
    
    for i in range(3, n+1):
        answer.append(answer[i-1] + answer[i-2])
    
    
    return answer[n] % 1234567