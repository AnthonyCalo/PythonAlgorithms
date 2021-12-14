class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        l, r=0, 1
        longest=0
        while r< len(s):
            left=False
            for i in s[l:r+1]:
                if(s[l:r+1].count(i)>1):
                    l+=1
                    left=True
                    break
            if(len(s[l:r+1])> longest):
                longest=r+1-l
            if(not left):
                r+=1
        return(longest)

'''
Problem explained in title
'''