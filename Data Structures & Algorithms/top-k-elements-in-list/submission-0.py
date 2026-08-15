class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        bignums = []
        while(k > 0):
            bignums.append(max(hash, key=hash.get))
            k -= 1
            del hash[max(hash, key=hash.get)]
        return bignums


