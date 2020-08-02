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

            loop through row of matrix:
              loop through col of matrix:
                if i or j is 0:
                  matrix[i][j] = 0 (the zero-out part)
                else:
                  if str1[i-1] == str2[j-1] NOTE: Pay close attention to the index values when comparing the chars at each index because i for matrix != i for str1, etc.
                    * matrix[i][j] = diagnonal value + 1
                  else:
                    matrix[i][j] = max(left neighbor, top neighbor)

            length = last value of the matrix (matrix[n-1][m-1])
            
            if length != Null:
              return length
            
            return 0 (this means there's no common subsequence)

            Time: O(n*m), n = len(text1), m = len(text2)
            Space: O(n*m)
      """


      col = len(text1) + 1
      row = len(text2) + 1
      
      matrix = [[None for i in range(col)] for j in range(row)]
      
      
      for i in range(row):
          for j in range(col):
              if i == 0 or j == 0:
                  matrix[i][j] = 0
              else: 
                  if text2[i-1] == text1[j-1]:
                      matrix[i][j] = matrix[i-1][j-1] + 1
                  else:
                      matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
                  
      length = matrix[-1][-1]
      
      if length != None:
          return length
      return 0
        
        
        