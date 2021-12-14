class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_pal=[]
        letters="abcdefghijklmnopqrstuvwxyz"
        nums="0123456789"
        for i in s:
            if( i.lower() in letters):
                check_pal.append(i.lower())
            if ( i in nums):
                check_pal.append(i)
        if len(check_pal)==0:
            return True
        return check_pal==check_pal[::-1]