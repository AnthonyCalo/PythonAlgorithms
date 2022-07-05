class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_sq_digits(x):
			# Helper function: Calculates the sum of the digits square: ie: 19 = 1**2 + 9**2
            result = 0
            while (x > 0):
                digit = x % 10
                x = x // 10
                result += digit ** 2
            return result
        hashset=[]
        while True:
            hashset.append(n)
            n=sum_sq_digits(n)
            if(n==1):
                return True
            if(n in hashset):
                return False
