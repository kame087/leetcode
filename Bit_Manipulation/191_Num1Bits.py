class Solution:
    def hammingWeight(self, n: int) -> int:

      """
        HIGH LEVEL:
          While n is > 0:
            check to see if least significant bit (LSB) is a 1 by using "&" bitwise operator and using 1 as a mask, 
            the result will be a 1 if the LSB is a 1, else 0.
            At every check add the result to your count variable.
            right shift n by 1 to check the next bit...

          return the count.

          * You can also use this approach to check the parity of a binary digit.

          Time: O(k), k = len of n
          Space: O(1)
      
      """
        
      count = 0
      
      while n:
          count += n & 1
          n >>= 1
          
      return count
        