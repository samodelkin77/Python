class Solution:

    def findMinMax (self, h):

        def setValue (a, b, func):
            if func (h [a], h [b]):
                return a
            else:
                return b

        mm = [{"min":-1, "max":-1}, {"min":0, "max":0}]
        for i in range (2, len (h)):
            j = i-1
            mm.append ({"min": setValue (j, mm [j] ["min"], lambda x, y: x < y), "max": setValue (j, mm [j] ["max"], lambda x, y: x >= y)})

        return mm
        

    def maxArea(self, height) -> int:
        mm = self.findMinMax (height)
        for i in range (len (height)):
            print (i, height [i], mm [i] ["min"], mm [i] ["max"])
        return -1



z = Solution()

#print (z.maxArea([1,8,6,2,5,4,8,3,7]))
#print (z.maxArea([1, 2, 4, 3]))
print (z.maxArea([8,10,14,0,13,10,9,9,11,11]))
#print (z.maxArea([1, 2]))