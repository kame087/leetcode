class Solution:
    def findMin(self, nums):
      """
        HIGH LEVEL:
        You want to perform a  binary search, but with a slight twist
        Instead of looking for a specific key, you're looking for the minimum, so you  want to compare the value @mid with hi bound element
        if mid > hi that's the search space you want to look at.
        otherwise look at the left search space

        PSEUDOCODE: 
        initialize lo with 0
        initialize hi with  len(A) - 1
        while lo < hi:
          calculate mid # (lo + hi) // 2
          if the number @mid is > then the number @hi:
              # this means that you want to perform a search on the side after index @mid
              make lo = mid +  1
          else: # which means that the lower number is on the left side of mid
              make hi = mid
        # eventually the while loop no longer meets the condition
        return A[lo] 

      """


        
      # think edge cases
      
      lo = 0
      hi = len(nums) - 1
      
      while lo < hi:
          mid = (lo + hi) // 2
          
          if nums[mid] > nums[hi]:
              lo = mid + 1
          else:
              hi = mid
          
                  
              
      return nums[lo]