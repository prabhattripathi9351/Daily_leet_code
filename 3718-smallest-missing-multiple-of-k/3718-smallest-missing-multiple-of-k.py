class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallest = 1
        kmultiple = set()
        for num in nums:
            if num % k == 0:
                kmultiple.add(num // k)
            if num // k == smallest:
                while smallest in kmultiple:
                    smallest += 1
        return smallest * k