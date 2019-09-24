class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = s + '#'
        currPos = 0
        # firstPos = 0
        foundChars = []
        lookingForChars = list (t)
        while currPos < len (s):
            print (currPos, s[currPos], foundChars)
            if s[currPos] in lookingForChars:
                foundChars.append ({"pos":currPos, "char":s[currPos]})
                lookingForChars.remove (s[currPos])
                if len (lookingForChars) == 0:
                    if len (result) > foundChars[-1]["pos"] - foundChars[0]["pos"]:
                        result = s[foundChars[0]["pos"]:foundChars[-1]["pos"]+1]
                    currPos = foundChars[0]["pos"]
                    lookingForChars.extend (foundChars[0]["char"])
                    foundChars.remove (foundChars[0])
            currPos += 1
        return result

z = Solution()

print (z.minWindow('ADOBECODEBANC', 'ABC'))