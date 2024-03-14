class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        temp = sorted(nums)
        current = {}
        ans = []
    

        for i in range(len(temp)):
            if temp[i] not in current:
                current[temp[i]] = i
        for idx in range(len(nums)):
            ans.append(current[nums[idx]])
        return ans