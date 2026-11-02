# 한 번호가 다른 번호의 접두어
# 접두어면 true 아니면 false
def solution(phone_book):
    answer = True
    
    # 딕셔너리 사용
    dict_phone = {}
    
    # 딕셔너리에 추가
    for phone in phone_book:
        dict_phone[phone] = dict_phone.get(phone, 0) + 1
    
    # 딕셔너리 검사 하나라도 있으면 true
    for phone in phone_book:
        
        nums = ''
        
        # 글자 하나씩 추가 하며 비교
        for num in phone:
            
            nums = nums + num
            
            
            if dict_phone.get(nums, 0) > 0:
                if nums != phone:
                
                    return False
    
    
    # 없으면 True
    
    return True