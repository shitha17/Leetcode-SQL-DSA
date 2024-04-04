class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start, sub_sum, count = 0,0,0

        for end in range(len(arr)):
            sub_sum += arr[end]

            if end-start+1 == k:
                if sub_sum/k >= threshold:
                    count+=1
                sub_sum -= arr[start]
                start += 1
        return count


