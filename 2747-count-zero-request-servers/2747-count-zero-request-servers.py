class Solution:
    def countServers(self, n, logs, x, q):
        a = l = r = 0 ; logs.sort(key=lambda k: k[1])
        qs = sorted(enumerate(q), key=lambda k: k[1])
        cnt, ans = [0] * (n + 1), [0] * len(q)
        for i, t in qs:
            while r < len(logs) and logs[r][1] <= t:
                s = logs[r][0]; cnt[s] += 1; r += 1
                if cnt[s] == 1: a += 1
            while l < r and logs[l][1] < t - x:
                s = logs[l][0]; cnt[s] -= 1; l += 1
                if cnt[s] == 0: a -= 1
            ans[i] = n - a
        return ans 