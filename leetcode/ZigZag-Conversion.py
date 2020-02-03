class Solution(object):
    def convert(self, s, numRows):
        
        if numRows == 1:
            return s
        charsZig = 2 * numRows - 2
        numZigs = int (len (s) / charsZig) + 1

        r = []
        for line in range (numRows):
            if line in (0, numRows - 1):
                lineLen = int (len (s) / charsZig) + 1
            else:
                lineLen =  numZigs * 2
            r.append(['_']* lineLen)
        # print (r)    

        for i in range (len(s)):
            posZig = i % charsZig
            if posZig < numRows:
                rowNumber = posZig
                if rowNumber in (0, numRows - 1):
                    j = int(i / charsZig)
                else:
                    j = int(i / charsZig) * 2
            else:
                # rowNumber = numRows - (charsZig - numRows) - 1
                rowNumber = numRows - (posZig - numRows) - 2
                j = int(i / charsZig) * 2 + 1
                # int(i / charsZig) +  i % charsZig - numRows + 2 * (int (i / charsZig) + 1)
            # print ("posZig=%i, %i %s -> %i,%i" % (posZig, i, s[i], rowNumber, j))
            r [rowNumber][j] = s [i]
        result = ""
        for y in r:
            result = result + "".join ([x for x in y if x!='_'])
        return result

z = Solution()

s = ''
numRows = 1
print (z.convert (s, numRows))