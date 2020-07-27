class Solution:
    def maxProduct(self, nums) -> int:
        
        """
          * HIGH LEVEL:
          * You want to follow a similar approach to Maximum subarray sum using Kadane’s algorithm. This will give you a Time Complexity of O(n) and Space: O(1)
          * have a global_max (which is what you’ll return)
          * a prev_max and prev_min to keep track of the maximum and minimum running products as you start multiplying in the current number.
          * !!!keep in mind that prev_min may be a negative number, and if the current number is also a negative, their product can become the maximum. (Another reason to keep track of prev_min)
          * iterate through the list starting with the second number:
              * have a current_min (which is the minimum product between: prev_min*num, prev_max*num, num
              * have a current_max (which is  the max product between: prev_min*num, prev_max*num, num
                  * NOTE: if num ends up being the value curr_max or curr_min, this signifies that you’re starting a new window.
              * update global_max which is the max between: global_max, curr_max
              * update prev_max with curr_max
              * update prev_min with curr_min
          * return global_max
            
        """
        
        output_max = nums[0]
        prev_max = nums[0]
        prev_min = nums[0]
        
        for i in range(1, len(nums)):
            curr_min =  min(prev_max*nums[i], prev_min*nums[i], nums[i])
            curr_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            output_max = max(output_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
            
        return output_max
        