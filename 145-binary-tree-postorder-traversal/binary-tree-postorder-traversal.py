# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def postorder(node):
        # если узел пустой
            if node is None:
                return
            
            postorder(node.left) # левое поддерево
            postorder(node.right) # правое поддерево
            result.append(node.val) # корень
        
        postorder(root)
        return result
        