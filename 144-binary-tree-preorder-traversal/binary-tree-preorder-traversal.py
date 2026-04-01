# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        result = []  
        
        def preorder(node):
            # если узел пустой
            if node is None:
                return
            
            result.append(node.val) # добавляем корень
            preorder(node.left) # левое поддерево
            preorder(node.right) # правое поддерево
        
        preorder(root) 
        return result