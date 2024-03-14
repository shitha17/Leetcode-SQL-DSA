class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in table:
                return [table[diff], i]
            table[nums[i]] = i
        
        return []
        
        
        