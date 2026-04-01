# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # ищем нужный узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:  # узел найден
            
            # нет левого поддерева
            if root.left is None:
                return root.right
            
            # нет правого поддерева
            if root.right is None:
                return root.left
            
            # если есть оба поддерева - ищем мин. справа
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            root.val = min_node.val
            
            # удаляем мин.узел
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root