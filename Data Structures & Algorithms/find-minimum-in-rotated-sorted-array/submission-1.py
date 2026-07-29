class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return(min(nums)) lol

        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            midpoint = (left + right) // 2
            res = min(res, nums[midpoint])
            if nums[midpoint] >= nums[left]:
                left = midpoint + 1
            else:
                right = midpoint - 1
        
        return res

            
