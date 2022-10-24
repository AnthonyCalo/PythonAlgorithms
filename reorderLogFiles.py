class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def isDigit(inputString) -> bool:
            si = inputString.split()
            for i in si[1:]:
                if(i.isdigit()):
                    return True
            return False
        dl = []
        ll = []
        for i in logs:
            if(isDigit(i)):
                dl.append(i)
            else:
                ll.append(i)
        
        ll.sort(key = lambda x: [x.split(" ")[1:],x.split(" ")[0]])
        for d in dl:
            ll.append(d)
        return ll
            

'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.

Return the final order of the logs.
'''