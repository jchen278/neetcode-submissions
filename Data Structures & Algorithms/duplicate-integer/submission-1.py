class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        bool = False
        length = len(nums)
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                bool = True
                return bool
        return bool

        