class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = added = 0
        for char in s:
            if char == "(":
                opened += 1
            elif opened:
                opened -= 1
            else:
                added += 1
        return added + opened

            


       