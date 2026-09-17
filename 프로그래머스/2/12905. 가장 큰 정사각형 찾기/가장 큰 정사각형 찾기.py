def solution(board):
    
    answer = 0
    
    # 각 칸에 "이 칸을 오른쪽 아래 꼭짓점으로 하는 최대 정사각형의 한 변"을 저장
    # 왼쪽 위 → 오른쪽 아래 순서로 순회하면서 이미 계산된 위/왼쪽/왼쪽위를 참고
    x = len(board)
    y = len(board[0])
    for i in range(x):
        for j in range(y):
            
            # 0인 칸은 정사각형이 될 수 없으니 패스
            if board[i][j] == 0:
                continue
            
            # 인덱스 에러 방지 존재하는 부분만 실행
            if i > 0 and j > 0:
                
                # 위, 왼쪽, 왼쪽위 세 칸 중 가장 작은 값 + 1
                # 셋 다 k 이상이어야 이 칸에서 (k+1)×(k+1)이 완성됨
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                
            # 한 변의 길이 최대 구하기
            answer = max(answer, board[i][j])
            
    # 한 변의 길이를 제곱해서 넓이 반환
    return answer ** 2