class Solution:
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        message = ""
        for word in strs:
            message += f"{len(word)}{self.delimiter}{word}"
        return message

    def decode(self, s: str) -> List[str]:
        messages = []
        index = 0
        while index < len(s):
            word_start = s.index(self.delimiter, index)
            word_length = int(s[index:word_start])
            messages.append(s[word_start + 1 : word_start + 1 + word_length])
            index = word_start + word_length + 1
        return messages