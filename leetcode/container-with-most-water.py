class Solution:
    
    def maxArea(self, height) -> int:
        m = 0
        for i, e in enumerate (height[:-1]):
            if (len (height) - i) * e > m:
                for j in range (i+1, len (height)):
                    if min (e, height[j]) * (j - i) > m:
                        m = min (e, height[j]) * (j - i)
        return m


z = Solution()

print (z.maxArea([1,8,6,2,5,4,8,3,7]))