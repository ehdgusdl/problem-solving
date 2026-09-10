def solution(brown, yellow):
    answer = []
    
    # 노란색 경우의 수 n x m 만큼 칠해짐
    # 범위 1 ~ 제곱근까지 해서 공약수 구하기
    num = []
    for i in range(1, int(yellow**0.5)+1):
        if (yellow % i) == 0:
            num.append([i, yellow // i])

    # n x m 일때 2n + 2m + 4 == brown
    for n, m in num:
        if ((2*n) + (2*m) + 4) == brown:
            if n >= m:
                answer.append(n+2)
                answer.append(m+2)
            else:
                answer.append(m+2)
                answer.append(n+2)

    
    
    return answer