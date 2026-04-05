from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            key = tuple(sorted(string))
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]

        return list(groups.values())