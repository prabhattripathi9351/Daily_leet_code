class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        seen = set()
        interval = []
        for i in range(len(s)):
            c = s[i]
            if c in seen:
                continue
            right = last[c]
            j = i + 1
            while j <= right:
                if s[j] in seen:
                    break
                right = max(right, last[s[j]])
                j += 1
            if j > right:
                interval.append([i, j - 1])
            seen.add(c)
        interval.sort(key=lambda x: x[1])
        last = -1
        res = []
        for l, r in interval:
            if l > last:
                last = r
                res.append(s[l:r + 1])
        return res