class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        for i in range(len(s)-1):
            l.append(ord(s[i])-ord(s[i+1]))
        c=0
        for i in l:
            c+=abs(i)
        return c