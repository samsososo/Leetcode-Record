# 3.Longest Substring without Repeating Characters

# Solution:
# Keep remove the first char in the str, array, list

class Solution:
    def lengthOfLongestSubstring(self, s):
        sub_str = ''
        max_len = 0

        for w in s:
            while w in sub_str:
                sub_str = sub_str[1:]
            else:
                sub_str += w
                max_len = max(len(sub_str), max_len)

        return max_len
