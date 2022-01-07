class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = ""
        s_len = len(s)
        idx=0
        src_index=0
        data = list(zip(indices, sources, targets))
        data.sort(key=lambda z:z[0])

        while idx< s_len and src_index<len(indices):
            if(idx == data[src_index][0]):
                src=data[src_index][1]
                src_len=len(src)
                s_val=s[idx: idx+src_len]
                if(s_val == src):
                    res+=data[src_index][2]
                else:
                    res+=s_val
                idx+=src_len
                src_index+=1
            else:
                res+=s[idx]
                idx+=1
        return res + s[idx:]
                
        