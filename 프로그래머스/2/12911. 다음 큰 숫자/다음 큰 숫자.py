def solution(n):
    
    # 다음수는 n보다 큼
    # 2진수 변환 했을떄 1의 개수 같음
    # n의 다음 큰 숫자는 조건을 만족하는 가장 작은 수 
    
    # 2진수에서 1의 개수
    target_count = bin(n).count('1')
    
    # n보다 최소 1 큼
    next_num = n + 1
    
    # 1의 개수가 같을때 까지 반복
    while bin(next_num).count('1') != target_count:
        
        # 1의 개수가 다르면 N + 1
        next_num += 1
    
    
    
    return next_num