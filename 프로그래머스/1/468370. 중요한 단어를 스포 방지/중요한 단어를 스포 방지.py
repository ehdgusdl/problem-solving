# 스포방지 왼쪽 -> 오른쪽 클릭해 중요한 단어 수 확인
# 단어는 공백 + 소문자 + 숫자
# 문자들의 인덱스 중 하나라도 스포 방지 구간이면 스포 방지 단어임
# 앞에선 스포 방지지만 뒤에 스포 방지가 아니면 중요 X
# 왼쪽 부터 판단

def solution(message, spoiler_ranges):
    answer = 0

    # 모든 단어를 리스트에 넣기
    word_list1 = message.split(' ')
    word_list2 = message.split(' ')
    
    idx = 0 # 시작 인덱스
    
    # 스포 방지 구간에 포함된 단어를 리스트에 넣기
    # word_list에 len으로 길이 수로 판단 끝나면 + 1 해서 다음 단어로 
    for word in word_list1:
        
        # word 단어 시작 지점 끝 지점에 인덱스가 겹치는지 
        for start, end in spoiler_ranges:
            
            end_idx = idx + len(word) -1
            
            # 범위 확인 start or end가 idx 안에 있어야 함
            if start <= end_idx and idx <= end:
                
                # 중요 단어 제거
                word_list2.remove(word)

                # 중요 단어 제거 헀는데 살아있다? 중요 X or 한번더 스포 방지
                # 단어를 뻇으니 다음 중복 단어 뺏을때 카운트 가능
                if word not in word_list2:
                    answer = answer + 1
                    
                # 현재 word는 추가 검사 X
                break
        
        # 다음 시작 단어의 알파벳 위치 (공백 고려) 
        idx = end_idx + 2
    
    
    return answer