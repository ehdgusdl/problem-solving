# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        answer = []
        
        # 재귀
        def dfs(depth, node):
            # 다음이 Null 이면 depth append 
            if node.left is None and node.right is None:
                answer.append(depth)
                return
            # left 부터 검사
            if node.left:

                # Null이 아니면 재귀
                dfs(depth + 1, node.left)

            if node.right:

                # Null이 아니면 재귀
                dfs(depth + 1, node.right)

        dfs(1, root)

        return max(answer)
        

        