class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(0, len(heights)):
            height = heights[i]
            for j in range(i+1, len(heights)):
                if height > heights[j]:
                    min(heights[i], heights[j])
                area = min(heights[i], heights[j]) * (j - i)
                if area > max:
                    max = area
        return max
