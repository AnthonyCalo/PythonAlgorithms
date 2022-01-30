class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = dict()
        sdict = dict()
        if(len(p)> len(s)):
            return []
        for i in range(len(p)):
            pdict[p[i]] = pdict.get(p[i],0)+1
            sdict[s[i]] = sdict.get(s[i],0)+1
        end = len(p)-1
        start = 0
        res = []
        while end< len(s):
            if(pdict==sdict):
                res.append(start)
            sdict[s[start]] = sdict.get(s[start],1)-1
            if(sdict[s[start]]==0):
                sdict.pop(s[start])
            start+=1
            end+=1
            if(end==len(s)):
                continue
            sdict[s[end]] = sdict.get(s[end],0)+1
            
        return(res)
        # this is esssentially a sliding window approach. Tests each string of length p in s with a dictionary to see if its
        # an anagram