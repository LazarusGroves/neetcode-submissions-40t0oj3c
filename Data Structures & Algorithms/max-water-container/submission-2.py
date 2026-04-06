class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            best = max(area, best)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best