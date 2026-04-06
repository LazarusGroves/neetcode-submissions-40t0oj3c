class Solution:
    def encode(self, strs: List[str]) -> str:
        message = ""
        for word in strs:
            message += f"{len(word)}x{word}"
        return message

    def decode(self, s: str) -> List[str]:
        messages = []
        index = 0
        while index < len(s):
            word_start = s.index("x", index)
            word_length = int(s[index:word_start])
            messages.append(s[word_start + 1 : word_start + 1 + word_length])
            index = word_start + word_length + 1
        return messages