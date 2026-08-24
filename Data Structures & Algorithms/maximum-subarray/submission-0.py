class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = 0
        maxSub = -100000
        for n in nums:
            sub += n
            if sub > maxSub:
                maxSub = sub            
            if sub < 0:
                sub = 0
        return maxSub