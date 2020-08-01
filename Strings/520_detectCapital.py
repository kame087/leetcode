class Solution:
    def detectCapitalUse(self, word: str) -> bool:

      """
        HIGH LEVEL:
          There's three cases that make the output true:
            if the first letter is a capital:
              - all subsequent letters have to be capital
                        OR
              - all subsequent letters have to be lowercase
            if the first letter is lowercase:
              - all subsequent letters have to be lowercase
        Time: O(n)
        Space: O(1)
      """
      
      firstCap = word[0] == word[0].upper()

      if firstCap:
        return word[1:] == word[1:].upper() or word[1:] == word[1:].lower()
      else:
        return word[1:] == word[1:].lower()

      
            
        
            
        
                
                
        