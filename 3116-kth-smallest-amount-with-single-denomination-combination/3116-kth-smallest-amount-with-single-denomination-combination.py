import math
class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        pie_terms = []
        for i in range(1, 1 << n):
            curr_lcm = 1
            set_bits = 0
            for j in range(n):
                if i & (1 << j):
                    curr_lcm = math.lcm(curr_lcm, coins[j])
                    set_bits += 1
            if set_bits % 2 == 1:
                pie_terms.append((curr_lcm, 1))
            else:
                pie_terms.append((curr_lcm, -1))
        low = 1
        high = min(coins) * k
        ans = high
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for lcm_val, sign in pie_terms:
                count += sign * (mid // lcm_val)
            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans