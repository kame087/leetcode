class Solution:
    def maxArea(self, height) -> int:
      """
        HIGH  LEVEL:
        The best approach that will give you a Time Complexity of O(n) is using the TWO POINTER TECHNIQUE:
        have a pointer starting at the far LEFT
        have a pointer starting at the far RIGHT
        while left doesn’t cross the right:
          calculate width based on difference between index values of left and right # width = right - left
          calculate “area” by multiplying width * the min value between elements @ left and @ right # max_water = max(max_water, width * min(water[left], water[right])
          move pointer with the smallest value
          i.e. if element @ left <= element @ right:
                  advance left
                otherwise:
                  advance right # decrease pointer value (right -= 1)
        
        return max_water
      
      """
        
      max_water = 0
      
      left = 0
      right = len(height) - 1
      
      while left < right:
          width = right - left
          max_water = max(max_water, (width*min(height[left], height[right])))
          if height[left] <= height[right]:
              left += 1
          else:
              right -= 1
              
      return max_water
  
      # Time: O(n)
      # Spae: O(1)