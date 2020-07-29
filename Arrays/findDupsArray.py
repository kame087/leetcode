class Solution:
    def findDuplicates(self, nums):

      """
        HIGH LEVEL:
          This is what I can come up with right off the bat. 
          * Have a hashmap that stores the values and their corresponding frequencies.
          * traverse through the list, and if the key has a frequency count > 1
          * add that key to the result list.
          * return the list.

          Complexities:
          Time: O(n), n = length of nums
          Space: O(n), n  = length of nums

      """
      freq = {}
      result = []
      
      for num in nums:
          if num not in freq:
              freq[num] = 0
          freq[num] += 1
          
      for key in freq:
          if freq[key] > 1:
              result.append(key)
              
      return result
    
        