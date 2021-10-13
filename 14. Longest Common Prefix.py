# ["flower","flow","flight"] -> "fl"
# ["dog","racecar","car"] -> ""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ["flower","flow","flight"]
        # ["dog","racecar","car"]
        minOfStrs = min(strs)  # aka the key
        maxOfStrs = max(strs)

        for i, c in enumerate(minOfStrs):
            if c != maxOfStrs[i]:
                return minOfStrs[:i]

        return minOfStrs
