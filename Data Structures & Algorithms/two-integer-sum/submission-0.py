class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}        

        for i in range(len(nums)):
            find = target - nums[i]
            if find in pairs.keys():
                return [pairs[find], i]
            
            pairs[nums[i]] = i