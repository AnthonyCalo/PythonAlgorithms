class Solution:
    def partitionString(self, s: str) -> int:
        last = []

        res = 0
        for i in range(len(s)):
            if(s[i] in last):
                res+=1
                last = [str(s[i])]
            else:
                last.append(s[i])
        res+=1
        return res
        