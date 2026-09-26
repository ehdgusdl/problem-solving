# 이번달 까지 기록으로 다음달 선물 순위 예측
# 선물이 더 많이 받은 A쪽이 다음달 선물을 받음
# 기록이 없거나 같으면 선물지수가 높은 사람이 받음 (선물 준 수 - 받은 선물)
# 선물 지수 까지 같으면 아무것도 안함
# 결과: 선물 제일 많이 받는 친구의 선물 수

# 친구들 이름, 선물 기록(준 사람, 받은 사람)
def solution(friends, gifts):

    num_f = len(friends)
    answer = [0] * num_f
    
    gift_log = {}
    
    # 선물 기록 정리하기
    # 리스트 [준사람, 받은사람, 횟수] 형식으로 바꾸기
    for item in gifts:
        giver, taker = item.split()
        pair = (giver, taker)
        
        gift_log[pair] = gift_log.get(pair, 0) + 1
    
    # 기본 딕셔너리
    gift_point = {} 
    
    for name in friends:
        gift_point[name] = [0, 0, 0]
    
    # 선물 지수 구하기
    # 리스트 [이름, 준 선물 수, 받은 선물 수, 선물 지수]
    for item in gifts:
        giver, taker = item.split()
        
        # 선물 준 경우
        gift_point[giver][0] = gift_point[giver][0] + 1
        gift_point[giver][2] = gift_point[giver][2] + 1
        
        # 선물 받은 경우
        gift_point[taker][1] = gift_point[taker][1] + 1
        gift_point[taker][2] = gift_point[taker][2] - 1
    
    # 반복문으로 사람들 받을 수 있는 선물 구하기
    for idx in range(num_f):
        give = friends[idx]
        
        for take in friends:
            
            # 자기 자신 패쓰
            if give == take:  
                continue
                
            pair1 = (give, take)
            pair2 = (take, give)
            
            # 선물 기록 판별
            give_count = gift_log.get(pair1, 0)
            take_count = gift_log.get(pair2, 0)
            
            if give_count > take_count:
                answer[idx] = answer[idx] +1
            
            # 선물 기록이 같으면 -> 선물 지수 판별
            elif give_count == take_count:
                
                if gift_point[give][2] > gift_point[take][2]:
                    answer[idx] = answer[idx] +1
        

    # 제일 많이 선물 받는 수 구하기
    return max(answer)