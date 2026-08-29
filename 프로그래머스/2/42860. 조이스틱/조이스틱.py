def solution(name):
    answer = 0
    num = len(name) - name.count("A") 
    if num == 0:
        return 0
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in name:
        idx = alp.index(i)
        answer += min(idx, 26 - idx)
        
    n = len(name)
    min_move = n - 1
        
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == "A":
            next_i += 1 
        
        min_move = min(min_move, 2 * i + (n - next_i), i + 2 * (n - next_i))

    return answer + min_move

