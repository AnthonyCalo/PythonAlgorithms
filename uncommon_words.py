class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words=s1.split()
        words2=s2.split()
        print(words, words2)
        return_list=[]
        for i in words:
            if(words.count(i)>1):
                continue
            if(i not in words2):
                return_list.append(i)
            else:
                words2.pop(words2.index(i))
        for j in words2:
            if(words2.count(j)==1 and j not in words):
                return_list.append(j)
        for k in return_list:
            k=str(k)
        return(return_list)
'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 

'''