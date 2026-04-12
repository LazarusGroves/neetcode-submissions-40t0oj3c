class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        window = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
            window[char] = 0

        needed = len(window.values())
        satisfied = 0
        smallest_substring = ""
        l = 0

        for index, char in enumerate(s):
            # Expand Right
            if char in window:
                window[char] += 1
                if t_dict[char] == window[char]:
                    satisfied += 1
            

            # Shrink Left
            while needed == satisfied:
                # Condition Satisfied, track smallest substring
                if len(s[l:index+1]) < len(smallest_substring) or smallest_substring == "":
                    smallest_substring = s[l:index+1]
                if s[l] in window:
                    if t_dict[s[l]] == window[s[l]]:
                        satisfied -= 1
                    window[s[l]] -= 1
                l += 1

        return smallest_substring


