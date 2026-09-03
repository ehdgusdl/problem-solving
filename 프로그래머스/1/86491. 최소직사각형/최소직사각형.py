def solution(sizes):
    answer = 0
    
    newsizes = []
    # 명함 가로 세로 기준 X 정렬 하여 가로 세로 다시 만들기
    for i in range(len(sizes)):
        newsizes.append(sorted(sizes[i]))
    
    x = 0
    y = 0
    
    # 제일 큰거 제일 작은거 곲하기
    for j in newsizes:
        x = max(x, j[0])
        y = max(y, j[1])
        
    
    return x*y