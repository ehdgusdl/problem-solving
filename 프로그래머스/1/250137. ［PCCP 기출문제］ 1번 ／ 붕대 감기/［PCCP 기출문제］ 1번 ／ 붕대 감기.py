# 붕대 t초 동안 1초마나 x만큼 회복 tx,  y 추가 회복
# 공격 당하거나 기술 끝 -> 붕대 감기 시전

# [시전 시간, 1초당 회복량, 추가 회복량] # 최대 체력 # 몬스터의 공격 시간과 피해량
def solution(bandage, health, attacks):
    now_health = health
    
    now = 0
    for time, dmg in attacks:
        
        print(now_health)
        #if (time - now) > 1:
        # 초당 회복하기
        now_health = now_health + bandage[1] * (time - now-1) 

        # 추가 회복
        now_health = now_health + bandage[2] * ((time - now -1) // bandage[0])

        # 최대 체력까지만 회복
        if now_health > health:
            now_health = health

            print(now_health)

        # 현재 시간 업데이트
        now = time

        # 피격
        now_health = now_health - dmg
        

        if now_health <= 0:
            return -1

    return now_health