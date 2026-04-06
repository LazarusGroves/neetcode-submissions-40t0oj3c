class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = ''.join(char for char in s if char.isalnum()).lower()
        length = len(normalized_s)
        for i in range(length // 2):
            if not normalized_s[i] == normalized_s[length - 1 - i]:
                return False
        
        return True