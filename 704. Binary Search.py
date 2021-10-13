class Solution:
    def search(self, nums: List[int], target: int) -> int:

        leftList = nums[0:len(nums) // 2]
        rightList = nums[len(nums) // 2:len(nums)]

        if target in leftList:
            return nums.index(target)
        elif target in rightList:

            return nums.index(target)
        else:
            return -1