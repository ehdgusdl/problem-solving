def solution(spell, dic):
    
    answer = 2
    
    # 길이 비교
    for word in dic:
        if len(spell) == len(word):
            
            all_w = True
            
            for alphabet in spell:
                 # 안들어간게 있는지 
                if alphabet not in word:
                    all_w = False
                    break
            if all_w == True:
                return 1
                
    return answer