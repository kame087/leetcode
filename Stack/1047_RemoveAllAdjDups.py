"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.


HIGH LEVEL:
  Initialize a stack
  push a buffer value to stack so that it's not empty because you'll need to peek at the stack

  traverse the string
  if current char is the same as the top value in stack
    pop top of stack
  otherwise
    push char to stack

  return a string version of stack starting from second position to omit the buffer value.

  COMPLEXITY:
    Time: O(n), n = len(S)
    Space: O(n) worst case if all chars don't have duplicate adjacent char.
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        stack = []
        stack.append(-1)
        
        for char in S:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
                
        return "".join(stack[1:])
        