class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = s + '#'
        currPos = 0
        insPos = 0
        # firstPos = 0
        foundChars = []
        lookingForChars = list (t)
        while currPos < len (s):
            if insPos < len (foundChars) and currPos > foundChars [insPos]["pos"]:
                insPos += 1
            print (currPos, s[currPos], foundChars, insPos)
            if s[currPos] in lookingForChars:
                # foundChars.append ({"pos":currPos, "char":s[currPos]})
                foundChars.insert (insPos, {"pos":currPos, "char":s[currPos]})
                lookingForChars.remove (s[currPos])
                if len (lookingForChars) == 0:
                    print ('Evrika!!! ', s[foundChars[0]["pos"]:foundChars[-1]["pos"]+1])
                    if len (result) > foundChars[-1]["pos"] - foundChars[0]["pos"]:
                        result = s[foundChars[0]["pos"]:foundChars[-1]["pos"]+1]
                    currPos = foundChars[0]["pos"]
                    lookingForChars.extend (foundChars[0]["char"])
                    foundChars.remove (foundChars[0])   
                    insPos = 0
            currPos += 1
        if len(result) > len (s):
            return ''
        else:
            return result

z = Solution()

# print (z.minWindow('ADOBECODEBANC', 'ABC'))
print (z.minWindow('aa', 'aa'))

#0123456789012
#ADOBECODEBANC

A: 0,10
B: 3,9
C: 5,12

# 0123456789012
# A  B C   BA C
