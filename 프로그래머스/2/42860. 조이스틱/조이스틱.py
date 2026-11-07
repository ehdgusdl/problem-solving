# A로만 이루워진 단어를 완성 name으로 바꿔야 함
# 몇번 이동 해야 하는지

def solution(name):
    
    
    answer = 0

    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    move = 20
    
    # for name
    for i in range(len(name)):
        
        # 상하 비교
        answer = answer + min(alp.index(name[i]),  26 - alp.index(name[i]))
        
        # 좌우 비교
        next_idx = i + 1
        
        # while A가 아닌 위치 찾기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx = next_idx + 1

        # next_idx를 찾았음  # 최대 한바퀴만 돌면 됨  
        # 왼쪽으로 갔다가 오른쪽으로 가는 거랑 
        # 오른쪽으로 갔다가 왼쪽으로 가는 거 비교 
        move = min(move, i * 2 + len(name) - next_idx, (len(name) - next_idx) * 2 + i)
        
        

    
    return answer + move