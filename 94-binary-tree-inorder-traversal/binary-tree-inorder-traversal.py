# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []  # список с ответом
        
        def inorder(node):
        # если узел пустой - ничего происходит
            if node is None:
                return
            
            inorder(node.left) # левое поддерево
            result.append(node.val) # добавляем значение узла
            inorder(node.right )# правое поддерево
        
        inorder(root)
        return result