class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = len(nums)*[1]
        n = len(nums)
        for i in range(1,n):
            left_array[i] = left_array[i-1]* nums[i-1]
        right_array = len(nums)*[1]
        for i in range(n-2,-1,-1):
            right_array[i] = right_array[i+1]*nums[i+1]
        ans = [left_array[i] * right_array[i] for i in range(n)]
            
        return ans