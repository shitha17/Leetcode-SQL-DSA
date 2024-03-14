class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        ans = []
        
        while left<=right:
            lsquare = nums[left]*nums[left]
            rsquare = nums[right]*nums[right]
            
            if rsquare > lsquare:
                ans.append(rsquare)
                right -= 1
            
            else:
                ans.append(lsquare)
                left += 1
            
        ans.reverse()
        return ans
                
            
            
            
        