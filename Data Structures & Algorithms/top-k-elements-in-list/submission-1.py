class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        sortedvalue = sorted(hash, key = hash.get, reverse = True) [:k]
        return sortedvalue
