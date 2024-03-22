class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num_map = {}
        for i in nums:
            if i not in num_map:
                num_map[i] = 1
            else: 
                num_map[i]+= 1
        for key,value in num_map.items():
            if value >2:
                return False
        
        return True
     