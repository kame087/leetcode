class Solution:
    # Leetcode # 54
    def spiralOrder(self, matrix):

      """
        HIGH LEVEL:
          You essentially want to append values to solution array in shells.
          Each shell is a value associated with top, bottom, left, or right.
          As you append the  values you want to update the shell value
          A special direction variable will let you know which direction you'll
          be iterating.

          initialize top and left to 0
          initialize bottom to len(matrix) i.e. row length
          initialize right to len(matrix[0]) i.e. column length

          while top doesn't cross bottom and left doesn't cross right:
            check direction value:
            if direction is 0:
              iterate from left to right and append nums of top level/shell
              then update (increase) top level by one
            else if direction is 1:
              iterate from top to bottom and append nums of right level/shell
              then update (decrease) right level by  one
            else if direction is 2:
              iterate from right to left and append nums of bottom level/shell
              then update (decrease) bottom level by one
            else if direction is 3:
              iterate from top to bottom and append nums of left level/shell
              then update (increase) left level by one
            update direction value by adding 1 to it and mod (%) by 4 to reset direction
          
          return spiral ordering.

      """
        
      if len(matrix) == 0:
          return []
      
      #output
      spiral = []
      
      # these will be the starting indices as we progress shell by shell
      top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
      
      direction = 0
      """
      direction will tell us which way to iterate:
      0: L -> R
      1: T -> B
      2: R -> L
      3: B -> T
      
      """
      
      while top <= bottom and left <= right:
          if direction == 0:
              # iterate from left to right and append nums of top level
              # then update (increase) top level by one
              for i in range(left, right+1):
                  spiral.append(matrix[top][i])
              top += 1
          elif direction == 1:
              # iterate from top to bottom and append nums of right level
              # then update (decrease) right level by one
              for i in range(top, bottom+1):
                  spiral.append(matrix[i][right])
              right -= 1
          elif direction == 2:
              # iterate from right to left and append nums of bottom level
              # then update (decrease) bottom level by one
              for i in range(right, left-1, -1):
                  spiral.append(matrix[bottom][i])
              bottom -= 1
          elif direction == 3:
              # iterate from bottom to top and append nums of left level
              # then update (increase) left level
              for i in range(bottom, top-1, -1):
                  spiral.append(matrix[i][left])
              left += 1
          direction  = (direction + 1) % 4
          
      return spiral
      
      
      
      