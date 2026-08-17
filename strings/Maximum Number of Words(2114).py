class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in range(len(sentences)):
            l=sentences[i].split()
            if len(l)>m:
                m=len(l)
        return m






        








        