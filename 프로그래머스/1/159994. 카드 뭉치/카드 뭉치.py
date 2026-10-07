def solution(cards1, cards2, goal):
    answer = []
    
    g_l = len(goal)
    
    
    for g in goal:
        
        
        # 다음에 올 수 있는게 없을때
        if cards1 and cards2 and g != cards1[0] and g != cards2[0]:
            return 'No'
        elif cards1 and g == cards1[0]:
            answer.append(cards1.pop(0))
            
        elif cards2 and g == cards2[0]: 
            answer.append(cards2.pop(0))
    
    if g_l == len(answer):
        return 'Yes'
    else:
        return 'No'
    
    return 'Yes'