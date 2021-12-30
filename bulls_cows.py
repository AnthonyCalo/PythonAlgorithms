class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sdict=dict()
        gdict=dict()
        #create 2 dicts witgh position as key and char as value
        for i,j in enumerate(secret):
            sdict[i]=j
            gdict[i]=guess[i]
        bulls=0
        cows=0
        for fuck in gdict:
            if(gdict[fuck]==sdict[fuck]):
                #if they are equal then one cow because in same spot. make in -999 so it doesn't effect next loop
                cows+=1
                sdict[fuck]=-999
                continue
            if(gdict[fuck] in sdict.values()):
                for key, val in sdict.items():
                    if(gdict[fuck]==val and gdict[key]!=sdict[key]):
                        bulls+=1
                        #removes duplicates so if the g has one 0 and s has 2 it isn't counted twice
                        sdict[key]=-99
                        break
        return (str(cows)+"A"+str(bulls)+"B")
            
    '''
    You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"'''