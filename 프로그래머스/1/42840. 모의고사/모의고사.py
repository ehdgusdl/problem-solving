def solution(answers):
    
    # 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    
    # 정답 횟수
    scores = [0, 0, 0]
    
    # 답 for문
    for idx, answer in enumerate(answers):
        
        if answer == patterns[0][idx % len(patterns[0])]:
            scores[0] += 1
            
        if answer == patterns[1][idx % len(patterns[1])]:
            scores[1] += 1
            
        if answer == patterns[2][idx % len(patterns[2])]:
            scores[2] += 1  
    
    # 가장 높은 점수 구하기
    max_score = max(scores)
    
    # 최고 점수자를 리스트에 담기
    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx + 1)
    
    
    return result