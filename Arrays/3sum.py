class Solution:
    def threeSum(self, nums):

      """
        HIGH LEVEL:
        The  problem set requires you  to return  unique triplets  of numbers in array that sum up to zero, or said target (if problem variant).
        The best way to approach this is to use a set initially so that it doesn’t count duplicates, and then return a list form of the set if a set is not allowed.
        This is a TWO POINTER approach:
            sort the array
            loop through each number up two 2 spots (to make up a triple)
              have two pointers: 
              a left = current_index + 1
              a right = len(array) - 1
              while left doesn’t cross right:
                sum up the three numbers
                if sum < target:
                  advance left pointer
                else if sum > target:
                  advance right pointer
                else the numbers sum up to target:
                  add numbers to set
                  advance left AND right pointer
      
      """
        
      solution = set()
      
      nums.sort()
      
      for i in range(len(nums) - 2):
          left = i + 1
          right = len(nums) - 1
          
          while left < right:
              total = nums[i] + nums[left] + nums[right]
              if total > 0:
                  right -= 1
              elif total < 0:
                  left += 1
              else:
                  solution.add((nums[i], nums[left], nums[right]))
                  left += 1
                  right -= 1
                  
      return solution
        
        
        