

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover=0
        if(len(digits)==1):
            if(digits[0]==9):
                return([1,0])
            else:
                return [(digits[0]+1)]
        for i in range(1, len(digits)+1):
            if(i==len(digits) and digits[-i]==9):
                digits.insert(0,1)
                digits[1]=0
                continue
                
            if(digits[-i]!=9):
                digits[-i]+=(1)
                return digits
            else:
                digits[-i]=0
                carryover=1
        return digits

'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [0]
Output: [1]
Explanation: The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].
'''


