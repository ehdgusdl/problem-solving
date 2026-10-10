def solution(s):
    answer = []
    
    s_word = s.split(" ")
    
    for word in s_word:
        answer.append(word.capitalize())
    
    return ' '.join(answer)