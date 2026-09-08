from itertools import permutations

# 소수 판별 함수
def isPrime(n):
    
    # 1 or 0은 소수 아님
    if n < 2:
        return False
    
    else:
        # 제곱 근을 기준으로 소수인지 판별
        for i in range(2, int(n**0.5) +1):
            
            if n%i == 0:
                return False
            
        return True

def solution(numbers):

    # 중복 방지
    nums = set()
    
    # 순열 조합 만들 숫자 개수
    for r in range(1, len(numbers) +1):
        
        # numbers에서 r개 만큼 숫자로 조합
        for p in permutations(numbers, r):
                   
            # int()로 0으로 시작 방지
            nums.add(int(''.join(p)))
    
    answer = 0
    # 만들어진 숫자 소수인지 판별
    for n in nums:
        if isPrime(n):
            answer = answer + 1              
                   
    return answer