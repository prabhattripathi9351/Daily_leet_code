class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        p = 0
        while p < n:
            c = ord(target[p]) - 97
            if cnt[c] == 0:
                break
            cnt[c] -= 1
            p += 1

        i = p
        while i >= 0:
            if i < n:
                t = ord(target[i]) - 97
                pick = -1
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        pick = c
                        break
                if pick >= 0:
                    cnt[pick] -= 1
                    tail = ''.join(chr(97 + c) * cnt[c] for c in range(26))
                    cnt[pick] += 1
                    return target[:i] + chr(97 + pick) + tail
            i -= 1
            if i >= 0:
                cnt[ord(target[i]) - 97] += 1
        return ""