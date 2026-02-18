class Solution:
    def search(self, nums, target):
        return self.binary(nums, target, 0, len(nums) - 1)

    def binary(self, nums, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.binary(nums, target, left, mid - 1)
        return self.binary(nums, target, mid + 1, right)


nums = [-1, 0, 3, 5, 9, 12]
print(Solution().search(nums, 9))
