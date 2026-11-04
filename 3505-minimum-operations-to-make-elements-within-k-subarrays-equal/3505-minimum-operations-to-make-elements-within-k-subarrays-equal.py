class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        lower = SortedList()
        upper = SortedList()
        lower_sum = 0
        upper_sum = 0
        min_ops = []

        for i, num in enumerate(nums):
            if not lower or num <= lower[-1]:
                lower.add(num)
                lower_sum += num
            else:
                upper.add(num)
                upper_sum += num
            
            if i >= x:
                out_num = nums[i - x]
                if out_num in lower:
                    lower.remove(out_num)
                    lower_sum -= out_num
                else:
                    upper.remove(out_num)
                    upper_sum -= out_num
            
            if len(lower) < len(upper):
                val = upper.pop(0)
                lower.add(val)
                upper_sum -= val
                lower_sum += val
            elif len(lower) - len(upper) > 1:
                val = lower.pop()
                upper.add(val)
                lower_sum -= val
                upper_sum += val
            
            if i >= x - 1:
                median = lower[-1]
                ops = (median * len(lower) - lower_sum) + (upper_sum - median * len(upper))
                min_ops.append(ops)
        
        m = len(min_ops)
        dp = [[math.inf] * (m + 2) for _ in range(k + 1)]

        for i in range(m + 2):
            dp[0][i] = 0

        for rem_k in range(1, k + 1):
            for i in range(m - 1, -1, -1):
                res = dp[rem_k][i + 1]

                next_idx = i + x
                if rem_k - 1 == 0:
                    future_cost = 0
                else:
                    future_cost = dp[rem_k - 1][next_idx] if next_idx <= m else math.inf
                
                res = min(res, min_ops[i] + future_cost)
                dp[rem_k][i] = res

        return dp[k][0]