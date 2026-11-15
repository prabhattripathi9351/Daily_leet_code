class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even, odd, parity, ans = 1, 0, 0, 0
        for x in arr:
            parity ^= (x & 1)
            if parity == 1:
                ans = (ans + even) % MOD
                odd += 1
            else:
                ans = (ans + odd) % MOD
                even += 1
        return ans