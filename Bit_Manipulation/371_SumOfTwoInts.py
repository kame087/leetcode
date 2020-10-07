class Solution:
    def getSum(self, a: int, b: int) -> int:

      """
        - HIGH LEVEL: Please note that for negative numbers, this approach will give a **TLE**
        - while **num2 ≠ 0,** You want to break down the addition process into 3 steps
          - Use **bitwise & with num1 and num2** to collect all the carry's and assign that to **carry**
          - Use **bitwise ^ with num1 and num2** to do the actual **addition** and assign it to **num1**
          - Use **bitwise <<** with **carry by 1,** and assign it to **num2**
        - return **num1**

      """
        
      while b != 0:
          carry = a & b
          
          a = a ^ b
          
          b = carry << 1
          
      return a
        