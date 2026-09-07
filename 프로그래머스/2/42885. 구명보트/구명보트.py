def solution(people, limit):
    
    answer = 0
    
    # 그리디 기본 정렬
    people.sort()
    left = 0
    right = len(people) -1
    
    # 매번 그때의 최선을 선택 가장 가벼운 + 가장 무거운
    while left <= right:


        # 제한과 비교 무거운 사람은 꼭 타야함
        if people[left] + people[right] <= limit:
            
            left = left + 1
            right = right - 1
            answer = answer + 1
            
            continue

        right = right - 1
        answer = answer + 1
        
    return answer