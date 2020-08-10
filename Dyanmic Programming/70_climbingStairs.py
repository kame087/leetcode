class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
            HIGH LEVEL:
                * This is a classic dynamic programming that mimics the fibonacci sequence problem.
                * Time: O(n), Space: O(n), n = number of steps.
                * The bottom-up approach to this problem is to create an array the  length of n+1 defaulting the values to 1.
                * arr[0], arr[1] = 1
                * iterate i from 2 -> n+1:
                    * arr[i] = arr[i-2] + arr[i-1]
                * return arr[n] # this will hold the number of ways to climb n stairs using 1 or 2 steps.
        
        """
        
        if n == 1:
            return 1
        
        stairs_steps = [1] * (n+1)
        
        for i in range(2, n+1):
            stairs_steps[i] = stairs_steps[i-2] + stairs_steps[i-1]
            
        return stairs_steps[n]
        