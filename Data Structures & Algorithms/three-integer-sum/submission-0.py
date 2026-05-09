class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []

        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue

            L = i + 1
            R = len(nums) - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                print(nums)
                print(nums[i], nums[L], nums[R])
                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                if sum < 0:
                    L += 1
                if sum > 0:
                    R -= 1
            i += 1
        return res