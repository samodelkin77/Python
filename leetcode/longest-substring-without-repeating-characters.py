class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        t = []
        for c in s:
            if c not in t:
                t.append (c)
            else:
                if len (t) > result:
                    result = len (t)
                t = t [t.index (c) + 1:] + [c]
        if len (t) > result:
                    result = len (t)
        return result
        

z = Solution()

print (z.lengthOfLongestSubstring (""))