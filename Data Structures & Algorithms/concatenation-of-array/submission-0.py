class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        for i in range(0, lenNums):
            nums.append(nums[i])
        return nums