class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max = min(map(len, strs))
        res = ""
        key = strs[0]
        for i in range(max):
            for j in range(len(strs)):
                if strs[j][i] != key[i]:
                    return res
            res += key[i]
        return res