# 1 ~ n번 n개 개인 정보 (약관 종류, 유효기간)
# 모든 달은 28일 

# 오늘 날짜, # 유효 기간, # 수집 일자
def solution(today, terms, privacies):
    answer = []
    
    m = len(privacies)
    d_terms = {}
    
    
    year, month, day = map(int, today.split('.'))
    today_list = year * 12 * 28 + month * 28 + day
    
    for item in terms:
        key, value = item.split()
        d_terms[key] = int(value)
    
    
    # 수집일자에 + 달수 > 오늘 날짜
    for cnt, privacie in enumerate(privacies):
        date, term = privacie.split()
        year, month, day = map(int, date.split('.'))
        expiration = year * 12 * 28 + month * 28 + day + d_terms[term] * 28
        
        # 날짜 비교 
        if expiration <= today_list:
            answer.append(cnt+ 1)
    
    
    
    # 파기 번호
    return answer