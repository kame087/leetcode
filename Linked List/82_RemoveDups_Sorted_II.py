"""
HIGH LEVEL:
  Create a hashmap that keeps track of number of occurence for each value in the linked list

  create a dummy node and initialize to 0
  create a prev node = to dummy # prev = dummy
  set prev.next to head
  create a traveling node and initialize to head # node = head
  traverse through the linked list # while node:
    check if node.val occurs more than once on hashmap # if freq[node.val] > 1:
      set a temp pointer to iterate freq[node.val] times # tmp = node
      for _ in range(freq[node.val]):
        tmp = tmp.next
      set prev.next to tmp # prev.next = tmp
      set node to tmp # node = tmp
    else:
      set prev to node # prev = node
      set node to node.next # node = node.next
  
  return dummy.next (which is head)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
           
        if head is None:
            return head
        
        freq = {}
        n = head
        
        # create a hashmap of occurences of each value in linked list
        while n:
            if n.val not in freq:
                freq[n.val] = 0
            freq[n.val] += 1
            n = n.next
            
        # start deleting nodes whose occurence is more than once
        dumb = ListNode(0)
        prev = dumb
        prev.next = head
        node = head
        while node:
            if freq[node.val] > 1:
                tmp = node
                for _ in range(freq[node.val]):
                    tmp = tmp.next
                prev.next = tmp
                node = tmp
            else:
                prev = node
                node = node.next
                
        return dumb.next
            
        
       
                
            