# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        """
            HIGH LEVEL:
                You're going to use a fast and slow pointer approach.
                Since you're deleting a node, you also want a prev pointer
                to attach it to  deletedNode's next node. i.e. prev.next = slow.next
                
                You essentially want to give the fast node a head start by advancing it
                n times.
                
                Then you're going to advance the slow and prev pointers until the fast pointer
                is done traveling the list.
                ** The fast node essentially is the trigger to where you're going to stop traveling.
                
                Ex:
                          F
                    1->2->3->4->5
    Next Iteration:        
                          F->F->F->F
                    P->P->P->S      <== S is the node you want to delete! 
                    
                
                if prev is still None, this means that you want to delete the head node,
                so just return head.next as head.
                
                After you stop traveling, assign prev.next as slow.next
                Return head.

                Time: O(n), since we're traveling the entire list with the fast pointer.
                Space: O(1), since we're not storing additional space as n scales up. It's always just three pointers.
                
        """
        
        if not head:
            return None
        
        
        counter = n
        fast = head
        
        while counter > 0:
            fast = fast.next
            counter -= 1
            
        prev = None   
        slow = head
        
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
            
        
        if not prev:
            return head.next
        
            
        prev.next = slow.next
        
        return head
            
        