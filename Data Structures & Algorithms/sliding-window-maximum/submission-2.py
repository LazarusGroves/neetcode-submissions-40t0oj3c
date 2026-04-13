from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxInts = []
        window = deque()
        for i in range(0, len(nums), 1):
            if len(window) > 0 and window[0] < i - k + 1:
                window.popleft()

            while len(window) > 0 and nums[i] >= nums[window[len(window) - 1]]:
                window.pop()

            window.append(i)

            if i >= k - 1:
                maxInts.append(nums[window[0]])

        return maxInts