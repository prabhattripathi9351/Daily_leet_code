class Solution:
    def minOperations(self, nums):
        n = len(nums)
        p = nums.index(0)
        inc = True
        dec = True
        for i in range(n):
            nxt = nums[(i + 1) % n]
            if nxt != (nums[i] + 1) % n:
                inc = False
            if nxt != (nums[i] - 1 + n) % n:
                dec = False
        ans = float('inf')
        if inc:
            ans = min(ans, p, n - p + 2)
        if dec:
            ans = min(ans, p + 2, n - p)
        return -1 if ans == float('inf') else ans