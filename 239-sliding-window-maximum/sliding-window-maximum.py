class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = 0
        ans = []
        d = deque()

        while j<len(nums):
            while len(d)>0 and d[-1]<nums[j]:
                d.pop()
            d.append(nums[j])
            if j-i+1 < k:
                j+=1
            elif j-i+1 == k:
                ans.append(d[0])
                if d[0]==nums[i]:
                    d.popleft()
                i+=1
                j+=1
        return ans

    
        