class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        len_ten_list=set()
        return_list=set()
        for i in range(len(s)-9):
            j=i+10
            if(s[i:j] in len_ten_list):
                return_list.add(s[i:j])
            else:
                len_ten_list.add(s[i:j])
        

        return(return_list)
'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]'''