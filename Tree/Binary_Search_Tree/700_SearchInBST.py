# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def searchBST(root, val):
  """
     HIGH LEVEL:
      Pretty straightforward, use binary search on the binary tree.
      The root is the mid that has been calculated for you.
      * Assign a node to root
      * while node exists:
        1. if node value is given value:
          * return node
        2. if node value is greater than given value
          * given value could possibly reside in left subtree
          * move node pointer to left 
        3. else node value is less than given value
          * given value could possibly reside in right subtree
          * move node pointer to right

      Time: O(log n), we're splitting our search space in half after every traversal, where n = size of tree.
      Space: O(1)
  
  """
    
  traveler = root
  
  while traveler:
      if traveler.val == val:
          return traveler
      elif traveler.val > val:
          traveler = traveler.left
      else:
          traveler = traveler.right
        
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


print(searchBST(root, 2)) # this will print the address, you can return traveler.val to see that it's the value



