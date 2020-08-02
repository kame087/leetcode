class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

      """
        HIGH LEVEL:
          ******* Brute Force Solution *********
          Time: O(m * n), m = length of row, n = length of col.
          Space: O(1)
          * count = 0
          * Traverse the entire matrix:
            if matrix[row][col] < 0:
              count += 1
            return count

          *************** Optimized Solution **************************
          There's this really cool optimized version that gives:
          Time: O(m + n), m = length of row, n = length of col
          Space: O(1)

          Credit to: @rock on leetcode for solution
          Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510249/JavaPython-3-2-similar-O(m-%2B-n)-codes-w-brief-explanation-and-analysis.

          Solution uses the fact that the negative regions form a staircase.
          ++++++
          ++++[--]
          ++++[--]
          +++[---]
          +[-----]  
          +[-----]

          You're going to start from the bottom staircase and check if the value is negative:
            if it is, then everything else is also negative, so count = count + len(grid[row][col:])
            update row value (row -= 1)
            otherwise: 
              update column value (col += 1)
          
          CODE:
            row_length = length(grid)
            row = row_length - 1 #starting index, since we're starting at the bottom of the "stairs"
            col = 0 # since we're starting with the closest step
            col_length = length(grid[0])
            count = 0

            while row >= 0 and col < col_length:
              if grid[row][col] < 0:
                count += len(grid[row][col:])
                row -= 1
              else:
                col += 1
            
            return count
      """
        
      count = 0
      
      for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] < 0:
                  count += 1 
              
      return count