class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        md=dict()
        for i in magazine:
            md[i]=md.get(i,0)+1
        for j in ransomNote:
            if(md.get(j, 0)==0):
                return False
            else:
                md[j]-=1
        return True
    
    '''
    Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
    '''