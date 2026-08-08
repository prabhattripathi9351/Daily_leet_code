class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        i, j = n - 1, m - 1
        last = [-1] * m
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
        ans = []
        skip = True
        j = 0
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif skip and (j == m - 1 or i < last[j + 1]):
                skip = False
                ans.append(i)
                j += 1
        return ans if j == m else []