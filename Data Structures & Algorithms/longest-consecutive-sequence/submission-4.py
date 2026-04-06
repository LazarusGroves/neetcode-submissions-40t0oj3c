class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val_set = set(nums)
        best = 0

        for val in val_set:
            if val - 1 not in val_set:
                length = 1
                while val + length in val_set:
                    length += 1
                best = max(best, length)

        return best