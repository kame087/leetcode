class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      """
        HIGH LEVEL:
          You're going to compare the sum that it's supposed to be, if all numbers were in the array vs the sum of the actual array.
          The difference is going to be the number that's missing.

          Iterate the array i: 0->n-1:
            *calculate the completeSum by adding the index value to it at every iteration.
            *calculate the actualSum by adding the element @index to it at every iteration.

          return completeSum - actualSum

          Time: O(n), n = len(array)
          Space: O(1), no extra memory needed except for the two variables we'll use to find the missing number.
      
      """

      completeSum = len(nums)
      actualSum = 0
      
      for i in range(len(nums)):
          completeSum += i
          actualSum += nums[i]
          
      return completeSum - actualSum
        