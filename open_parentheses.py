def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    symbols={
        "(":")",
        "[": "]",
        "{": "}" 
    }
    openers=[]
    pairs_open_length=0
    for i in s[0]:
        print(i, "i")
        if(i == "(" or i=="[" or i=="{"):
            print(i)
            pairs_open_length+=1
            openers.append(i)
    #this scenario first character isn't an opener. return false
    if(openers==[]):
        print("here")
        return False
    
    counter=0
    for j in s:
        counter+=1
        if(j=="]" or j=="}" or j==")"):
            opposite = symbols.keys()[symbols.values().index(j)]
            if(opposite==openers[-1]):
                openers.pop(openers.index(openers[-1]))
        
    if(openers==[]):
        return True
    else: 
        return False
    print(pairs_open_length, openers[0], "openers 0")

print(isValid(["()[]{}"]))