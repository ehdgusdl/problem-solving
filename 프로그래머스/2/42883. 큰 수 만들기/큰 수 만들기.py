def solution(number, k):
    
    # 남길 숫자를 순서대로 쌓는 스택
    stack = []
    
    # 앞에서 부터 숫자 검증
    for d in number:
        
        # 앞 숫자 < 뒤 숫자이면 앞의 숫자를 지우기
        while k > 0 and stack and stack[-1] < d:
            
            # 이전 숫자 제거
            stack.pop()
            
            # 시도횟수 차감
            k = k -1
        
        # 현재 숫자는 일단 남김
        stack.append(d)
    
    # 못 지웠으면 뒤에서부터 k개 제거
    if k > 0:
        stack = stack[:-k]    
    
    return ''.join(stack)