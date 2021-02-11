from math import ceil

class Solution(object):

    def median (self, nums) -> int:
        l = len (nums)
        if l == 0:
            m = 0
        else:
            if l % 2 == 0:
                m = (nums [int (l / 2)] + nums [int (l / 2) - 1]) / 2
            else:
                m = nums [int ((l - 1) / 2)]
        return m

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i = 10
        r = -1
        n = len (nums1)
        m = len (nums2)
        l1, r1, l2, r2 = 0, n-1, 0, m-1
        while r1 - l1 > 0 and r2 - l2 > 0 and i > 0:
            i -= 1
            p1, p2 = ceil (l1 + (r1 - l1) / 2), ceil (l2 + (r2 - l2) / 2)
            print ('l1: %i, r1: %i, p1: %i, l2: %i, r2: %i, p2: %i' % (l1, r1, p1, l2, r2, p2))
            if nums1 [p1] > nums2 [p2]:
                l2 = p2
            else:
                l1 = p1
        return r

        
z = Solution()
nums1 = [2, 4, 6, 8, 14]
nums2 = [5, 7, 9, 11, 13]
#nums1 = [1]
#nums2 = [2, 3, 5, 6, 7]


print (z.findMedianSortedArrays(nums1, nums2))


