class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 1
        for x in nums:
            dp[x + 1] = dp.get(x, 0) + 1   # use x as x+1 (must come first)
            dp[x] = dp.get(x - 1, 0) + 1   # keep x as x
            ans = max(ans, dp[x], dp[x + 1])
        return ans