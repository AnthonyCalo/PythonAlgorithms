# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if(x==0):
#             return 0
#         if(x==1):
#             return 1
#         if(x==2 or x==3):
#             return 1
#         for i in range(x):
#             if(i*i==x):
#                 return(i)
#             elif(i*i>x):
#                 return(i-1)
from os import TMP_MAX


def fib(n):
    print("called", n)
    if(n<3):
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print("resut",fib(6))
n =9
a, b =1,1

while n>2:
    temp =b
    b = a+b
    a=temp
    n-=1

print(b)
