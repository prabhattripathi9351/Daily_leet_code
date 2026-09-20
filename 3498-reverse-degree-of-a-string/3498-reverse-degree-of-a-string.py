class Solution(object):
    def reverseDegree(self, s):
        return sum((123 - ord(c)) * (i + 1) for i, c in enumerate(s))