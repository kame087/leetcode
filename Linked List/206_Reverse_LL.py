# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

      """
        HIGH LEVEL:
        * This was kinda tricky to wrap my head around but I think I got it.
        * This is my linear approach, with a Time complexity of O(n) and Space of O(1):
        * create the traveling node and assign it as head # curr = head
        * create a previous node and assign it to NULL # prev = None
        * traverse the linked list while the current node exists:
            * create a temp node and assign it as current’s next pointer # temp = curr.next
            * assign current’s next as the previous node # curr.next = prev
            * assign previous node as the current node # prev = curr
            * move on to the next node, which means assigning curr to temp # curr = temp
        * return prev (since curr at this point, points to NULL)

      """
        
      curr = head
      
      prev = None
      
      while(curr):
          temp = curr.next
          curr.next = prev
          prev = curr
          curr = temp
          
      
      
      return prev