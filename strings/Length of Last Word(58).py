class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=list(s.split())
        c=0
        for i in l[len(l)-1]:
            c+=1
        return c