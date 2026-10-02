# 테이블, 정수 타입 컬럼 # 2차원 행렬
# 열은 컬럼, 행은 튜플
# 첫 번째 컬럼은 기본 키로서 중복되지 않게 보장

# col은 컬럼 값을 기준으로 오름차순 # 동일시 첫번째 컬럼의 값을 기준으로 내림차순
# 정렬된 데이터에서 S_i를 i번째 행의 튜플에 대해 각 컬럼을 i로 나눈 값들의 합
def solution(data, col, row_begin, row_end):
    answer = 0
    
    # data 정렬 튜플로
    # 겹치면 1번 인덱스로 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    # s_i 다 더하기
    for i in range(row_begin, row_end + 1):
        
        s_i = sum(val % i for val in data[i - 1])
        
        answer ^= s_i
    
    return answer