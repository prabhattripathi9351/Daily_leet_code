class Solution:
    def maxLength(self, nums: List[int]) -> int:
        mask = [0, 0, 1, 2, 1, 4, 3, 8, 1, 2, 5]
        used = l = 0
        ans = 2
        for r, x in enumerate(nums):
            while used & mask[x]:
                used ^= mask[nums[l]]
                l += 1
            used |= mask[x]
            ans = max(ans, r - l + 1)
        return ans