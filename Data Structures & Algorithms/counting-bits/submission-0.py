class Solution:
    def countOnes(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(n + 1):
            res.append(self.countOnes(i))
        return res