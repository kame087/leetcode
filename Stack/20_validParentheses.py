class Solution:
    def isValid(self, s: str) -> bool:

      """
        HIGH LEVEL:
          I feel like whenever a problem is asking if the pairs are valid. You should always take advantage of a stack.
          * One quick sanity check is to see if the input string is even, if it isn't, it's automatically false.

          Here's the approach:
          create a hashmap that stores the closing bracket as the key and the opening bracket as the value.
          initialize a stack

          traverse the string 
            if the char is a value:
              push it onto the stack
            else: (this means it's a closing bracket)
              if the stack is not empty:
                peek the top and see if it's the corresponding opening bracket
                  if it is, pop it from the stack.
                else:
                  return False

          if the stack is empty: 
            return True
          
          return False (this means each opening bracket is missing its pair)

        Time: O(n)
        Space: O(n)

      """

      symbols = {')': '(', '}': '{', ']': '['}
      
      stack = []

      if len(s) % 2 != 0:
            return False
        
      for char in s:
          if char in symbols.values():
              stack.append(char)
          elif char in symbols:
              if len(stack) != 0:
                  if stack[-1] == symbols[char]:
                      stack.pop()
              else:
                  return False
      if len(stack) == 0:
          return True
      else:
          return False
        
      
      
            
        
        
        
        