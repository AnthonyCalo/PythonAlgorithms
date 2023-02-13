
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        countDict = dict()
        for char in s:
            countDict[char] = countDict.get(char, 0) + 1
        vals = countDict.values()
        vals.sort(reverse=True)
        res = 0
        while len(vals) > 0:
            cur = vals.pop(0)
            if(cur not in vals):
                continue
            else:
                while cur in vals:
                    res+=1
                    cur-=1
                if(cur!=0):
                    vals.append(cur)
        return res



'''
647. Minimum Deletions to Make Character Frequencies Unique
Medium
3.2K
49
Companies

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:
'''