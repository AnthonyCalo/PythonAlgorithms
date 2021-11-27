'''
An image smoother is a filter of the size 3 x 3 that can be
 applied to each cell of an image by rounding down the average 
 of the cell and the eight surrounding cells (i.e., the average of 
 the nine cells in the blue smoother). If one or more of the surrounding cells 
 of a cell is not present, we do not consider it in the average (i.e., the average of 
 the four cells in the red smoother).
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
'''
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m=len(img)
        n=len(img[0])
        averages = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
#up, down, left, right, upright, upleft, downrihgt, downleft
                neighbors=[[i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j+1],[i-1,j-1],[i+1,j+1],[i+1,j-1]]
                summ=img[i][j]
                counter=1
                for k in neighbors:
                    if 0<=k[0]<m and 0<=k[1]<n:
                        summ+=img[k[0]][k[1]]
                        counter+=1
                    else:
                        continue
                average=summ//counter
                averages[i][j]=average
        return averages

                