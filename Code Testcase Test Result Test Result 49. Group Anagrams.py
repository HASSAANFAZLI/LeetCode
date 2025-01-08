class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

            res.setdefault(tuple(count), []).append(str)

        return res.values()
