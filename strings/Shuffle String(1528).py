class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=[""]*len(s)
        for i in range(len(s)):
            l[indices[i]]=s[i]
        res=""
        for i in l:
            res+=i
        return res