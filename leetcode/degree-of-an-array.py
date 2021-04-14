class Solution:
    def findShortestSubArray(self, nums) -> int:
        fh, l, r = {}, {}, {}
        max_degree  = 0
        for i, e in enumerate (nums):
            if e not in fh:
                fh [e] = 0
                l [e] = i
            fh [e] += 1
            r [e] = i
            if fh [e] > max_degree:
                max_degree = fh [e]
        # print (fh, max_degree)
        # print (l)
        # print (r)
        min_length = len (nums)
        for i in fh.keys():
            if fh [i] == max_degree:
                if r [i] - l [i] + 1 < min_length:
                    min_length = r [i] - l [i] + 1
        return min_length

z = Solution()
print (z.findShortestSubArray ([1,2,2,3,1,4,2]))
