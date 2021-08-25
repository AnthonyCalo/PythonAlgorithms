class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Takes a string as input. Then returns the longest substring without repeating characters
        """
        if len(s)<2:
            return len(s)
        elif len(s)==2 and s[0]==s[1]:
            return 1
        else:
            longestSub = []
            i =0
            j =1
            try:
                if(s[i]==s[i+1]):
                    print("RIGHT HERE MOTHAFUCKA")
                    i+=1
                    j+=1
            except Exception:
                pass


            while j< len(s):
                if i ==j:
                    j+=1
                sub = s[i:j+1]

                repeat = False
                for item in sub:
                    if sub.count(item) > 1:
                        i=i+sub.index(item)+1

                        repeat=True
                        break
                if repeat==False:
                    if len(sub) > len(longestSub):
                        longestSub=sub
                    j+=1
                print(sub)
            return len(longestSub)

    

                
sol = Solution()
sol.lengthOfLongestSubstring("adfdsfoiuepwadcniopewe")