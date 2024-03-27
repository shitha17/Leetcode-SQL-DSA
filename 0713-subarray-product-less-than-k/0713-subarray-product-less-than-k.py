class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res,l,r,p = 0,0,0,1
        
        while r<len(nums):
            p *= nums[r]
            while r >= l and p >= k:
                p /= nums[l]
                l += 1
            res += r-l+1
            r += 1
        return res
            