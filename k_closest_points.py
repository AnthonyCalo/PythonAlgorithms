import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #this function gets the difference between x and y for the distance function
        def dif(p1, p2):
            x_dif=p1[0]-p2[0]
            y_dif=p1[1]-p2[1]
            return [x_dif, y_dif]
        res={}
        for i in range(len(points)):
            #diffence between x and y on point and 00
            diffs=dif([0,0], points[i])
            #distance function sqrt((x1-x2)**2 + (y1-y2)**2)
            difference=math.sqrt(diffs[1]**2 + diffs[0]**2)
            res[i+1] = difference
        #sort a dictionary of each point and its distance by distance
        sorted_res=dict(sorted(res.items(), key=lambda item: item[1]))
        resL=[]
        #return the result list resL after appending the points in 
        for i in sorted_res:
            resL.append(points[i-1])
        return resL[0:k]



'''Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).'''