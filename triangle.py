#******************************************************************************
# triangle.py
# Name: Anthony Calo
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://stackoverflow.com/questions/967661/python-truncate-after-a-hundreds
#https://learnandlearn.com/python-programming/python-reference/find-inverse-sine-arc-sine-python-using-asine-function
#both of those to learn acos and asin
import math


print('Enter 3 side lengths in descending order')

c = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
a = float(input("Enter the third side: "))
   
#law of cosine = c**2 = a**2 + b**2 - 2abCos(C)
#c1 is equal to -2abcos(C)
C1 = c**2 - (a**2 + b**2)
#c2 is equal to cos(C)
C2 = (C1)/(-2 * a* b)
C = math.acos(C2)
C = math.degrees(C)
#law of sines c/sinC = b/ sinB
# sin b = sinc * b / c
#convert sinc to radians
B1 = math.sin(math.radians(C))
B2 = (B1 * b) / c
#b2 = sinB
B = math.asin(B2)
#B = math.degrees(B)

A = 180 - (B + C)
if b > c or a > b or a<0 or a + b <= c:
    print(""" If the side lengths entered are either not all positive,
          aren’t entered indescending order, or don’t satisfy the triangle inequality""")
else:
    print("The angles are: ")
    print(C)
    print(B)
    print(A)
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#


