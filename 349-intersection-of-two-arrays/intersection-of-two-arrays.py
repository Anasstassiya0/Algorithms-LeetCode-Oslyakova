class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table = {}
        result = []

        for num in nums1:
            hash_table[num] = True

        for num in nums2:
            if num in hash_table:
                result.append(num)
                
                del hash_table[num]  
        return result