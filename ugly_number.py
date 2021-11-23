# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        while n%2==0 and n!=1:
            n=int(n/2)
            if n==1:
                return True
        while n%3==0 and n!=1:
            n=int(n/3)
            if n==1:
                return True
        while n%5==0 and n!=1:
            n=int(n/5)
            if n==1:
                return True
        return False