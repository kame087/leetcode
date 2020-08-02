class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      """
        HIGH LEVEL:
          I remember this problem from my algorithms class, and it requires a dynamic programming strategy.

          Create a matrix based on the lengths of each input string + 1 and default the values at each slot to NULL:
            i.e.
              col = text1.length + 1 # m
              row = text2.length + 1 # n
            The reason for this is because we want to zero out the zero indices of the matrix so we have a default value
            from where to start from.

            loop through length of text2:
              loop through length of text1:
                if str1[i] == str2[j] NOTE: Pay close attention to the index values when comparing the chars at each index because i for matrix != i for str1, etc.
                  * matrix[i+1][j+1] = diagnonal value + 1 (matrix[i][j] + 1)
                else:
                  matrix[i+1][j+1] = max(left neighbor, top neighbor) # max(matrix[i+1][j], max[i][j+1])

            return the last element in the matrix (matrix[-1][-1])

            Time: O(n*m), n = len(text1), m = len(text2)
            Space: O(n*m)
      """
      
      
      col = len(text1) + 1
      row = len(text2) + 1
        
      matrix = [[0 for i in range(col)] for j in range(row)]
        
        
      for i in range(len(text2)):
        for j in range(len(text1)):
          if text2[i] == text1[j]:
            matrix[i+1][j+1] = matrix[i][j] + 1
          else:
            matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
          
      return matrix[-1][-1]
        
        
        