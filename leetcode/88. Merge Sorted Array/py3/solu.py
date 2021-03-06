# start from the end
# Interview Tip: This is a medium-level solution to an easy-level problem. Many of LeetCode's easy-level problems have more difficult solutions, and good candidates are expected to find them.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # set p1 and p2 to point to the end of their corresponding arrays.
        p1 = m - 1
        p2 = n - 1
        # And move p backwords through the array, each time writing 
        # the smallest value pointed at by p1 or p2
        for p in range(n + m - 1, -1, -1):
            # 
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # move p1
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # move p2
                nums1[p] = nums2[p2]
                p2 -= 1

# #
# # start from the beginning
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # Make a copy for the first m elements
#         nums1_copy = nums1[:m]
#         # read pointers for
#         p1, p2 = 0, 0
#         # compare elements from nums1copy and nums2 and write smallest to nums1
#         for p in range(n + m):
#             # we also need to ensure that p1 and p2 aren't over boundaries
#             if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
#                 nums1[p] = nums1_copy[p1]
#                 p1 += 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 += 1
        