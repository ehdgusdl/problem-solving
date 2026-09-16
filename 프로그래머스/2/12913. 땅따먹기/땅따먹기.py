def solution(land):
    answer = 0

    # for문으로 land 크기만큼
    for i in range(1, len(land)):
        
        # 같은 열을 제외한 인덱스 max로 비교 4개 열
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[-1])