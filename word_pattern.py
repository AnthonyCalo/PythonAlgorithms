# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternList=[]
        for i in pattern:
            patternList.append(i)
        slist=s.split(" ")
        
        oneway, otherway= {}, {}
        if(len(slist)!= len(patternList)):
            return False
        for c1, c2 in zip(patternList, slist):
            if((c1 in oneway and oneway[c1]!=c2 )or( c2 in otherway and otherway[c2]!=c1)):
                return False
            oneway[c1]=c2
            otherway[c2]=c1
        return True
        