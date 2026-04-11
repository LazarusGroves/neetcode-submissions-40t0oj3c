from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        best = 0

        for char in s:
            seen[char] += 1

            while sum(seen.values()) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1

            best = max(best, sum(seen.values()))
            
        return best