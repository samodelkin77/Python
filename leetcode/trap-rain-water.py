import logging

logger = logging.getLogger()

class Solution(object):
    def trace (self, s):
        # pass
        print (s)

    def sign (self, i):
        if i > 0:
            return 1
        elif i < 0:
            return -1
        else:
            return 0

    def findNextPoint (self, index, firstTime = False):
        self.trace ('*** findNetxPoint: %i' % index)
        result = -1
        mi = -1
        okToExit = firstTime
        if index < self.height_len - 1:          
            for i in range (index + 1, self.height_len):
                self.trace ('i=%i h[i]=%i h[i-1]=%i h[index]=%i mi=%i result=%i' % (i, self.height [i], self.height [i - 1], self.height [index], mi, result))
                if self.height [i - 1] < self.height [i]:
                    okToExit = True
                if self.height [i - 1] > self.height [i] and i > index + 1 and okToExit:
                    if self.height [i - 1] > self.height [mi]:
                        mi = i - 1
                    if self.height [i - 1] >= self.height [index]:
                        result = i - 1
                        break
                # self.trace ('i=%i h[i]=%i h[i-1]=%i updown=%i' % (i, self.height [i], self.height [i - 1], updown))
                # if self.sign (self.height [i] - self.height [i - 1]) == updown:
                #     if updown < 0:
                #         result = i - 1
                #         break
                #     else:
                #         updown = -1
            self.trace ('!!! mi = %i, result = %i !!!' % (mi, result))
            if result == -1 and mi > 1:
                self.trace ('*** findNetxPoint.mi = %i' % mi)
                result = mi
            elif result == -1 and okToExit:
                result = self.height_len - 1
        self.trace ('*** findNetxPoint.result = %i' % result)
        return result

    def getSum (self, l, r):
        self.trace ('*** getSum: %i:%i' % (l, r))
        result = 0
        m = min (self.height [l], self.height [r])
        for i in range (l +1, r): 
            if self.height [i] < m:
                result += m - self.height [i]
        self.trace ('*** getSum.resut =: %i' % result)                
        return result
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height = [0] + height + [0]
        self.height_len = len (self.height)
        result = 0
        leftPoint = self.findNextPoint(0, True)
        if leftPoint > -1:
            while leftPoint < self.height_len - 1:
                rightPoint = self.findNextPoint(leftPoint)
                if rightPoint == -1:
                    break
                result += self.getSum (leftPoint, rightPoint)
                leftPoint = rightPoint
        return result


a = [1, 0, 1]
#a = [5,4,0,2]
#a = [0,1,0,2,1,0,1,3,2,1,2,1]
#a = [5,2,1,2,1,5]
z = Solution()
print (z.trap (a))