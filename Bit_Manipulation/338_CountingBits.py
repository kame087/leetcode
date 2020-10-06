class Solution:
    def countBits(self, num: int) -> List[int]:

      """
        HIGH LEVEL: 
          Similar approach to counting 1 bits of a number (Leetcode # 191)

          The only difference is you're doing it for a list of numbers given the last number from 0 -> number

          It's best to modularize the counting of 1 bits of a number to a function, so that you just call that function as you loop through
          every number.

          Time: O(n*k), n = list of nums you have to loop, k = length of each number represented as a binary digit.
          Space: O(n), if we account for the list of 1 bit counts, we have to return.
      
      """
        
      def count_ones(number, ones_count):
          num_bits = 0
          while number:
              num_bits += number & 1
              number >>= 1
          ones_count.append(num_bits)
      
      ones_count = []
      
      for i in range(num+1):
          count_ones(i, ones_count)
          
          
      return ones_count
    
    
        