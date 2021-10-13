class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        for i in range(1, len(nums)):
            if nums[head] != nums[i]:
                head += 1
                nums[head]= nums[i]
        return head + 1
