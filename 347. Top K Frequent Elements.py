class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        hashmap = dict(Counter(sorted(nums)))

        for key,value in hashmap.items():
            freq[value].append(key)


        res = []
        for i in range(len(freq)-1,0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
