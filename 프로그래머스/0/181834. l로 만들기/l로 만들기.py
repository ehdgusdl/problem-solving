def solution(myString):
    answer = ''
    
    for i in myString:
        if i < 'l':
            answer = answer + 'l'
        else:
            answer = answer + i
    
    return answer