
'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).'''


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		nums1.extend(nums2)
		nums1 = (sorted(nums1))
		if len(nums1) % 2 == 0:
			a = nums1[int(len(nums1) / 2)]
			b = nums1[int(len(nums1) / 2 - 1)]
			res = float(( a + b) / 2)

		else:
			s = int(len(nums1) / 2)
			res = float(nums1[s])

		return res
