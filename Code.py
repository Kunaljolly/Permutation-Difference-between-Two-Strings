class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        l = s
        s = {x:(list(s).index(x)) for x in s}
        t = {x:(list(t).index(x)) for x in t}
        c = 0
        for x in l:
            if s[x] - t[x] > 0:
                c += (s[x] - t[x])
            else:
                c += -1*(s[x] - t[x])
        return c
