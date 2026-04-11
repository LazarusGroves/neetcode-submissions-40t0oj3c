class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_checklist = {}
        window = {}
        for char in s1:
            s1_checklist[char] = s1_checklist.get(char, 0) + 1
            window[char] = 0
        
        matches = 0
        l = 0

        for index, char in enumerate(s2):
            if char in s1_checklist:
                window[char] += 1
                if window[char] == s1_checklist[char]:
                    matches += 1

            while index - l >= len(s1):
                if s2[l] in s1_checklist:
                    if window[s2[l]] == s1_checklist[s2[l]]:
                        matches -= 1
                    window[s2[l]] -= 1
                l += 1

            if matches == len(s1_checklist):
                return True
        
        return False
