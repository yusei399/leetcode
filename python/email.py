import re

class Solution:
	def check(self, s: str) ->bool:
		return True if (len(s) >= 12          and
						re.search('[a-z]', s) and
						re.search('[A-Z]',s) and
						re.search('[0-9]', s) and
						re.search('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~]',s))else False

if __name__ == "__main__":
	s = Solution()
	string_1 = "" #False
	string_2 = "abcd" #False
	string_3 = "abcdefghijklmn"
	string_4 = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	# string_5 =
	# string_6 =
	print(s.check(string_1))
	print(s.check(string_2))
	print(s.check(string_3))
	print(s.check(string_4))
	# print(s.check(string_5))
