class Solution:
    def parsePattern (self, p: str):
        result = []
        for c in p:
            if c != '*':
                result.append ({"c": c, "m": True})
            else:
                result [-1] ["m"] = False
        return result
        
    def isMatchRecurse (self, s: str, p) -> bool:
#        print ("start: ", s, p)
        i, j = 0, 0
        while i < len (s) and j < len (p):
#            print (i, s [i], j, p[j]["c"], p[j]["m"])        
            if p [j] ["c"] in ['.', s [i]]:
                if p [j] ["m"] == True:
                    j += 1
                    i += 1
                else:
                    return self.isMatchRecurse (s[i+1:], p[j:]) or self.isMatchRecurse (s[i:], p[j+1:])
            elif p [j] ["c"] != s [i] and p [j] ["m"] == False:
                j += 1
            else:
                return False
#        print (i, j)
        if i == len (s):
            for e in p[j:]:
                if e ["m"] == True:
                    return False
            return True
        else:
            return False


    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatchRecurse (s, self.parsePattern (p))

z = Solution()

def runTests():
    global z
    testCases = [
        ["aa", "a", False],
        ["aa", "a*", True],
        ["aaa", "a*b", False],
        ["aaa", "a*a", True],
        ["ab", ".*", True],
        ["aab", "c*a*b", True],
        ["mississippi", "mis*is*p*.", False],
        ["aaa", "aaaa", False],
        ["bbbba", ".*a*a", True]
    ]    
    for t in testCases:
        if z.isMatch (t[0], t[1]) != t [2]:
            print ("!!! ", t [0], t[1])

runTests()

#print (z.isMatch ("bbbba", ".*a*a"))
#print (z.isMatch ("a", ".*a*a"))


