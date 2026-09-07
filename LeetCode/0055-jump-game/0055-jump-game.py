from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0

        for i, jump in enumerate(nums):

            # 인덱스가 최대 도달 거리 보다 크면 False
            if i > max_reach:
                return False

            # 아니면 최대 도달거리 업데이트 
            max_reach = max(max_reach, i + jump)

            # 최대 도달 거리 이상이면 True
            if max_reach >= len(nums) -1:
                return True
