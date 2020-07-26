"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:


Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:


Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.

HIGH LEVEL:
  Basically obtain a global total value
  and a leftSum tracker # this keeps track of a sum as you iterate from left to right
  traverse from left to right:
    if the running leftSum is equal to the globalSum - the leftSum - (currentNumber):
      you've found the pivot index
    otherwise update leftSum with adding the currentNumber
  
  if you haven't found the pivot index by now....return -1

"""


def pivotIndex(nums):
    
    total = sum(nums)
    leftSum = 0
    
    for i in range(len(nums)):
        if leftSum == (total - leftSum - nums[i]):
            return i
        leftSum += nums[i]
        
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6])) #should return 3
print(pivotIndex([1, 2, 3])) #no pivot index...return -1

