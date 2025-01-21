'''
1849. Splitting a String Into Descending Consecutive Values
Solved
Medium
Topics
Companies
Hint

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

    For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
    Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.

Return true if it is possible to split s as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.

'''
class Solution:
    def splitString(self, s: str) -> bool:
        for substring in range(1, len(s)):
            subs = s[:substring]
            next_idx = 0
            sn = int(subs)
            last_idx = substring
            sn-=1
            next_idx, there = self.look_for_num(s[substring:], sn) 
            sn-=1
            last_idx += next_idx
            if last_idx >= len(s) -1 and there:
                return True
            while there:
                next_idx, there = self.look_for_num(s[last_idx+1:], sn)
                if not there:
                    continue
                sn -=1
                last_idx += next_idx+1
                if  last_idx >= len(s) - 1:
                    return True

        return False
        
    def look_for_num(self, s2: str, num: int):
        numstring = str(num)
        ns_len = len(numstring)
        if ns_len > len(s2):
            return 0,False
        elif ns_len == len(s2):
            return ns_len, numstring == s2
        ns_idx = 0
        leading_zero = True
        for idx, char in enumerate(s2):
            if leading_zero and char == "0":
                continue
            if char != numstring[ns_idx]:
                return 0, False
            elif char == numstring[ns_idx]:
                if ns_idx == ns_len -1:
                    return idx,True
                leading_zero = False
                ns_idx += 1
            else:
                return 0, False
        if num == 0:
            return 10000, True
        else:
            return 0, False
                
            


