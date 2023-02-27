from operator import le
from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		nums_len = len(nums)
		for i in nums:
			for j in nums:
				print(nums[j + 1])
				# if nums[i] == nums[j + 1]:
				# 	nums[j + 1]

if __name__ =="__main__":
	s = Solution()
	list = [1, 2,5 ,4,5,5 ]
	print(s.removeDuplicates(list))