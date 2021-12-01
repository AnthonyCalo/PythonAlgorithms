class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = "qwertyuiopQWERTYUIOP"
        middle="asdfghjklASDFGHJKL"
        bottom ="zxcvbnmZXCVBNM"
        return_list=[]
        for word in words:
            samerow=True
            first_letter_row=''
            if(word[0] in top):
                first_letter_row=top
            elif(word[0] in middle):
                first_letter_row=middle
            else:
                first_letter_row=bottom
            for letter in word:
                if(letter not in first_letter_row):
                    samerow=False
            if(samerow):
                return_list.append(word)
        return(return_list)
                