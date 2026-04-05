from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+ 1)]

        for num, count in Counter(nums).items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0 , -1):
            result.extend(freq[i])
            if len(result) >= k:
                return result[:k]