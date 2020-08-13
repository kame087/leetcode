# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        # Time: O(n)
        # Space: O(n)
        
        inorder = []
        stack = []
        
        if root is None:
            return inorder
        
        while (root != None or len(stack) != 0):
            while root != None:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
            
        return inorder