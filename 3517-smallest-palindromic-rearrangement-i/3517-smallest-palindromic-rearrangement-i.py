from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        left_half = []
        middle = ""
        for ch in sorted(freq):
            even_freq = freq[ch] // 2
            
            left_half.append(ch*even_freq)
            if freq[ch]%2 != 0:
                middle = ch
        left_half = "".join(left_half)
        return left_half + middle + left_half[::-1]
        