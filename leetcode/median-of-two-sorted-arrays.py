class Solution(object):
    def median (self, nums):
        l = len (nums)
        if l == 0:
            m = 0
        else:
            if l % 2 == 0:
                m = (nums [int (l / 2)] + nums [int (l / 2) - 1]) / 2
            else:
                m = nums [int ((l - 1) / 2)]
        return m

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m1 = self.median (nums1)
        m2 = self.median (nums2)
        if m1 > m2:
            m1, m2, nums1, nums2 = m2, m1, nums2, nums1
        elif m1 == m2:
            return m1

        if len (nums1) == 0:
            r = m2
        elif len (nums2) == 0:
            r = m1
        elif nums1 [-1] < nums2 [0]:
            r = self.median (nums1 + nums2)
        else:
            l2 = len (nums2)
            r = m2 - (l2 % 2) / 2
            i = int (l2  / 2)
            while i > 0 and nums2 [i] >= m1:
                i -= 1
                r -= 0.5

        return r

        
z = Solution()
# nums1 = [2, 4, 6, 8]
# nums2 = [5, 7, 9, 11, 13]
nums1 = []
nums2 = [1]


print (z.findMedianSortedArrays(nums1, nums2))