class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_Text = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        
        for c in balloon:
            res = min(res, count_Text[c]//balloon[c])
        return res
                
        