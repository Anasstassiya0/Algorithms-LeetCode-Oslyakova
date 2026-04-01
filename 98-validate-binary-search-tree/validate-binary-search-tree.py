# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        
        def check(node, min_val, max_val):
            if node is None:
                return True
            
            # проверка диапазона
            if not (min_val < node.val < max_val):
                return False
            
            # проверка левого и правого поддерева
            return (
                check(node.left, min_val, node.val) and
                check(node.right, node.val, max_val)
            )
        
        return check(root, float('-inf'), float('inf'))
        