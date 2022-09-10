class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
        return len(nums)


if __name__ == "__main__":
	s = Solution()
	nums = [1, 2 ,4]
	target = 3
	print(s.searchInsert(nums, target))
