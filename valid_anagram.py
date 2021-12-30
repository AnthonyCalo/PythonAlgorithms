class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict=dict()
        tdict=dict()
        if(len(s)!=len(t)):
            return False
        # create dictionary of character counts. if the dicts are equal its an anagram
        for i in range(len(s)):
            sdict[s[i]]=sdict.get(s[i],0)+1
            tdict[t[i]]=tdict.get(t[i],0)+1
        return sdict==tdict