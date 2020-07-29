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

    def findDuplicatesOptimized(self, nums):
        """
            HIGH LEVEL:
                Traverse the list i = 1 to n:
                    index = abs(element@i) - 1
                    go to that index, if element @index < 1:
                        add abs(element@i) to result
                    otherwise:
                        convert element@index to a negative value
                
                return result

                Complexities:
                    Time: O(n)
                    Space, O(1)

        """

        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 1:
                result.append(abs(nums[i]))
            else:
                nums[index] *= -1

        return result
    
        