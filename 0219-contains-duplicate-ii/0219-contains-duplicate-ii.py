class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        
        for index,value in enumerate(nums):
            if value in dic and abs(index- dic[value] <= k):
                return True
            dic[value] = index
        return False
        