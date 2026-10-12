# x의 모든 0을 제거합니다.
# X길이 C X를 C를 2진법으로 표현 한 문자열
def solution(s):
    
    cnt = 0
    cnt0 = 0
    
    # while 1이 될때까지
    while s != '1':
        cnt = cnt + 1
        
        # 이진수 변환
        cnt0 = cnt0 + s.count('0')
        
        # 이진수를 길이로
        c = len(s) - s.count('0')
        
        s = format(c, 'b')
    
    
    # 이진 변환 수 + 제거된 0 개수
    return [cnt, cnt0]