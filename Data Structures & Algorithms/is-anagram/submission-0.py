class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        if (len(s) != len(t)):
            return False

        for index, letter in enumerate(s):
            if letter in seen_s:
                seen_s[letter] += 1
            else:
                seen_s[letter] = 1
        
        for index, letter in enumerate(t):
            if letter in seen_t:
                seen_t[letter] += 1
            else:
                seen_t[letter] = 1

        for letter in seen_s:
            if letter not in seen_t:
                return False
            if seen_s[letter] != seen_t[letter]:
                return False

        return True
            
        