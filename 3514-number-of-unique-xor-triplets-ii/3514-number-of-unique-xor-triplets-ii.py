class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        set_1 = set()
        n = len(nums)
        for i in range(n):
            for j in range(i , n):
                set_1.add(nums[i]^nums[j])
        ans = set()
        for x in set_1:
            for num in nums:
                ans.add(x^num)
        return len(ans)