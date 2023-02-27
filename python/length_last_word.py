class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		return len(s.rstrip(' ').split(' ')[-1])

if __name__ == "__main__":
	s = Solution()
	print(s.lengthOfLastWord("Hello world"))