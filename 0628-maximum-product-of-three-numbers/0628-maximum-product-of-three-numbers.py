class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        opt_1 = nums[0]*nums[1]*nums[2]
        opt_2 = nums[-1]*nums[-2]*nums[0]
        return max(opt_1 , opt_2)
