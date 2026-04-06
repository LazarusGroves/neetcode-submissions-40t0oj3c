class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        for l in range(len(heights)):
            for r in range(l + 1, len(heights), 1):
                area = min(heights[l], heights[r]) * (r - l)
                best = max(area, best)


        return best