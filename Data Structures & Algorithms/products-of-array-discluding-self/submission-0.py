class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            answer[i] = pre
            pre *= nums[i]
        suff = 1
        for i in range(len(nums)):
            answer[len(nums) - i - 1] *= suff
            suff *= nums[len(nums) - i - 1]

        return answer
        

