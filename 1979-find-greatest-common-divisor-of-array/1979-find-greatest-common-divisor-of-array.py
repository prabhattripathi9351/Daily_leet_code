import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minium = min(nums)
        maximum = max(nums)
        return math.gcd(maximum , minium)