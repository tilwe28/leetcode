class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2,  nums1

        n, m = len(nums1), len(nums2)
        half = (n + m) // 2

        l, r = 0, n - 1
        while True:
            i = (l + r) // 2
            j = ((n + m) // 2) - i - 2

            left1 = nums1[i] if i >= 0 else float("-infinity")
            right1 = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            left2 = nums2[j] if j >= 0 else float("-infinity")
            right2 = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")
            if left1 <= right2 and left2 <= right1:
                if (n + m) % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1