class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

      """
        HIGH LEVEL:
          This problem is pretty straightforward.
          Have a hashmap and store the numbers with their respective frequency.

          Go through the hashmap and check their frequencies.
          If any of the numbers' frequency is > 1:
            return True

          otherwise return False

          Time: O(n)
          Space: O(n)
      
      """
        
      if len(nums) == 0:
          return False
      
      freq = {}
      
      for num in nums:
          if num not in freq:
              freq[num] = 0
          freq[num] += 1
          
      for key, value in freq.items():
          if value > 1:
              return True
          
      return False