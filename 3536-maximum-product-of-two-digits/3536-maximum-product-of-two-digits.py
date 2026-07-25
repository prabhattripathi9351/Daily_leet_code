class Solution:
    def maxProduct(self, n: int) -> int:
        new_num = [int(x) for x in str(n)]
        new_num.sort(reverse=True)
        return new_num[0] * new_num[1]
        
