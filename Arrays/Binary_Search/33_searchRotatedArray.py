class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
            HIGH LEVEL:
                We want to perform a modified binary search to find the smallest element
                set smallest element as "start"

                Reset low and high to default values
                Determine which search space to perform a regular binary search by comparing if target is in between A[start:high+1]
                  set lo = start
                otherwise:
                  search space on the left could potentially have the target value
                  set high = start
                
                then off that info we can perform a regular binary search

                Time: O(log n)
                Space: O(1)
        
        """
        if nums is None or len(nums) == 0:
            return -1 
        
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid =  (lo + hi) // 2
            
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
                
        start = lo # this is the index of the smallest number
        
        lo = 0
        hi = len(nums) - 1
        
        if nums[start] <= target <= nums[hi]: # if target is within this search space
            lo = start # set lo to start
        else:
            hi = start # this means the target could potentially be in the left search space
        
        # perform regular binary search
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
                