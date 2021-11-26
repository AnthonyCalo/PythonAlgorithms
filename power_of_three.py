class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<3):
            if(n==1):
                return True
            return False
        done=False
        while not done:
            if(n==3):
                return True
            if(n%3!=0):
                return False
                done=True
            else:
                n=n/3
        return False