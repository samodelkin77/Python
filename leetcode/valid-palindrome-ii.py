# from math import ceil

    class Solution(object):
        def validPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            result = True
            i = 0
            j = len (s) - 1
            si = -1
            sj = -1
            while i <= j:
                # print ('i=%i, j=%i, s[i]=%s, s[j]=%s' % (i, j, s[i], s[j]), s [i] == s [j])
                if s [i] == s [j]:
                    i += 1
                    j -= 1
                else:
                    if sj > -1:
                        i = i - (sj -j) + 1
                        j = sj
                        # print ('Rollback: i=%i, j=%i' % (i, j))
                    if si > -1:
                        j = j + (i - si) - 1
                        i = si
                        # print ('Rollback: i=%i, j=%i' % (i, j))
                    if si < 0 and s [i + 1] == s [j]:
                        si = i
                        i += 1
                    elif sj < 0 and s [i] == s [j-1]:
                        sj = j
                        j -= 1
                    else:
                        result = False
                        break
                    # print ('si=%i, sj=%i' % (si, sj))
            return result


z = Solution()
print (z.validPalindrome ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
