class Solution(object):
	def mergeTwoLists(self, list1, list2):
		self.list1 = list1
		self.list2 = list2
		list2_len = len(self.list2)
		total_len = len(self.list1) + list2_len
		i = 0
		while(i < list2_len):
			self.list1.append(list2[i])
			i += 1
		i = 0
		while(i < total_len - 1):
			if self.list1[i] > self.list1[i + 1]:
				self.list1[i], self.list1[i + 1] = self.list1[i + 1], self.list1[i]
			i += 1
		return self.list1



if __name__ == "__main__":
	s = Solution()
	list1 = [1,2, 3]
	list2 = [4,5,6]
	print(s.mergeTwoLists(list1, list2,)) 