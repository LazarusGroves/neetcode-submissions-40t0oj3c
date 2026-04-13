class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxInts = []
        for i in range(0, len(nums) - k + 1, 1):
            maxInts.append(max(nums[i:i+k]))
        return maxInts