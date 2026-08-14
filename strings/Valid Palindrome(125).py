class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                x+=i.lower()
        y=""
        for i in range(len(x)-1,-1,-1):
            y+=x[i]
        if x==y:
            return True
        else:
            return False