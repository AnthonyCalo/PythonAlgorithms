class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if(rowIndex==0):
            return ([1])
            
        output=[[1], [1,1]]
        
        for i in range(2, rowIndex+1):
            output.append([1])
            m=1
            n=0
            while m<len(output[i-1]):
                output[i].append(output[i-1][m]+output[i-1][n])
                m += 1
                n += 1
            output[i].append(1)
        return output[-1]
                