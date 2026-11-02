def solution(phone_book):
    
    # 전체 번호를 셋에 저장 → 조회 O(1)
    phone_set = set(phone_book)          
    
    # 번호를 하나씩 검사
    for number in phone_book:            
        
        # 길이 1부터 (전체길이-1)까지의 접두사 검사
        for i in range(1, len(number)):  
            
            # 그 접두사가 셋 목록에 있으면
            if number[:i] in phone_set:  
                
                # 접두사 관계 발견 → 실패
                return False
            
    # 루프 끝이면 접두사 없는거         
    return True