class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        rets=[]
        if digits=="":
            return []
        #this function basically calls itself for every possible
        #lettercombination. Then appends it to return string if length equals
        #length of digits
        def dfs(index=0, prevStr=""):
            if(index==len(digits)):
                rets.append(prevStr)
                return
            for i in range(len(mapping[str(digits[index])])):
                #call dfs with increase index and each letter for this number appended to prevStr
                dfs(index+1,( prevStr+mapping[str(digits[index])][i]))
        dfs()
        return(rets)

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters."""