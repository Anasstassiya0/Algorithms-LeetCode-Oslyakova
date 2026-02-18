class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        last_nums1 = m - 1
        last_nums2 = n - 1
        insert_pos = m + n - 1

        while last_nums1 >= 0 and last_nums2 >= 0:
            if nums1[last_nums1] > nums2[last_nums2]:
                nums1[insert_pos] = nums1[last_nums1]
                last_nums1 -= 1
            else:
                nums1[insert_pos] = nums2[last_nums2]
                last_nums2 -= 1
            insert_pos -= 1

        while last_nums2 >= 0:
            nums1[insert_pos] = nums2[last_nums2]
            last_nums2 -= 1
            insert_pos -= 1

