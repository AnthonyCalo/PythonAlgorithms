# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        true_count=[]
        for i in word:
            if(ord(i)> 96 and ord(i)<123):
                capital=False
                true_count.append(False)
            else:
                capital=True
                true_count.append(True)
        if(true_count.count(True)==len(word) or true_count.count(True)==0):
            return True
        elif(true_count.count(True)==1):
            return(true_count[0])            
        else:
            return False
        