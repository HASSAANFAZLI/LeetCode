class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = False
        x = len(nums)
        for i in range(x):
            for l in range(i + 1, len(nums)):
                if nums[i] + nums[l] == target:
                    return (i, l)

            x = x - 1
