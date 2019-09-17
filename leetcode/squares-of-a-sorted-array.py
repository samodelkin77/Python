class Solution(object):

    def binarySearch (self, A, v, l = 0, pr = -1):
        result = -1
        if pr == -1:
            r = len (A) - 1
        else:
            r = pr 
        # (l, r) = (0, self.A_len - 1)        
        while result < 0:
            if r - l == 1 or r == l:
                if A [l] >= v:
                    result = l
                else:
                    result = r
                break
            i = l + (int)((r -l) / 2)
            # print ('l=%i r=%i i=%i' % (l, r, i))
            if A [i] == v:
                result = i
            elif A [i] > v:
                r = i
            else:
                l = i
        # print ('result for %i in (%i, %i) is %i' % (v, l, r, result))
        return result    

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        pi = self.binarySearch(A, 0)
        ni = pi - 1
        result = []
        while ni >= 0 and pi < len(A):
            # print ('ni=%i pi=%i A[ni]=%i A[pi]=%i' % (ni, pi, A[ni], A[pi]))
            if abs (A[pi]) > abs(A [ni]):
                result.append (A [ni] * A [ni])
                ni -= 1
            else:
                result.append (A [pi] * A [pi])
                pi += 1
            print (result)
        # print ('ni = %i pi = %i' % (ni, pi))
        if ni < 0:
            for i in range(pi, len(A)):
                result.append (A[i] * A [i])
        elif pi >= len (A):
            for i in range(ni, -1, -1):
                result.append (A[i] * A [i])
        return result

"""
    def sortedSquares(self, A):
        self.A = A + [1e20]
        result = [0]
        i = len(A)-1
        while A [i] >= 0 and i >= 0:
            result.insert (1, A [i] * A [i])
            i -= 1
        result.append (1e20)
        if i >= 0:
            if len(result) == 2:
                for elem in A:
                    result.insert (1, elem*elem)
            else:
                index = len (result)-1
                for elem in A [:i+1]:
                    qelem = elem * elem
                    while qelem < result [index]:
                        index -= 1
                    result.insert (index + 1, qelem)
        return result [1:-1]
"""


def runTests (z):
    tests = [
        {'param':[-4,-1,0,3,10], 'result':[0,1,9,16,100]},
        {'param':[-2,-1,3], 'result':[1,4,9]},
        {'param':[-1], 'result':[1]},
        {'param':[-2,0], 'result':[0,4]},
        {'param':[-1,2,2], 'result':[1,4,4]},
        {'param':[-5,-4,-3,-3,5], 'result':[9,9,16,25,25]}
    ]
    for test in tests:
        result = z.sortedSquares (test["param"])
        if result != test["result"]:
            print ("Zhopa. Input:", test["param"], ' output:', result, ' expected:', test["result"])

z = Solution()
# a = [-2, 0]

# print (z.sortedSquares (a))
runTests (z)