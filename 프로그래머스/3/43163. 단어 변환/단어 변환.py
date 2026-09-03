# 알파벳 하나만 바꾸기
# word에 있는 단어로 변경
from collections import deque


def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    
    q = deque()
    q.append((begin, 0))
    
    while q:
    
        now, step = q.popleft()
        
        if target == now:
            return step
        
        # 하나만 같은지 확인
        for word in words:
            cnt = 0
            
            for i in range(len(now)):
                if now[i] == word[i]:
                    cnt = cnt + 1
                
            if cnt == len(now) -1:
                q.append((word, step +1))

