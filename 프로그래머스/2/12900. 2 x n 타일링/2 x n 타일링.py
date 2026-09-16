# 피보나치 수열
# 시작시 세로로 시작 or 가로로 시작
# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5

def solution(n):
    
    answer = [0, 1, 2]
    
    if n <= 2:
        return answer[n]
    
    for i in range(3, n+1):
        answer.append((answer[i-1] + answer[i-2])% 1000000007)
    
    return answer[n] 