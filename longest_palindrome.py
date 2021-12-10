class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        #this helper functions finds the longest palindrome with l,r in the center
        def helper(l, r):
            #if s[r]==s[l] go one more away in the list
            while (l >= 0 and r < len(s) and s[r] == s[l]):
                l-=1 
                r+=1
            return s[l + 1: r]
        ret=""
        
        for i in range(len(s)):
            midpal=helper(i,i)
            if(len(midpal)> len(ret)):
                ret=midpal
            #this second midpal is incase 2 letter are at the center of palindrome
            # example 'abba'
            midpal=(helper(i, i+1))
            if(len(midpal)> len(ret)):
                ret=midpal
        return ret
