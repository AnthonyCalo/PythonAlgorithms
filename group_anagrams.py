# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newStrs=[]
        final_list=[]
        for i in strs:
            sortedString=("".join(sorted(i)))
            if(sortedString in newStrs):
                continue
            else:
                newStrs.append(sortedString)
                final_list.append([])
        
    #still linear time complexity because the second loop makes in O(2n) not O(n**2))
        for i in strs:
            sortedString2=("".join(sorted(i)))
            final_list[newStrs.index(sortedString2)].append(i)
        return(final_list)
            
