def merge(intervals):
    intervals.sort()
    counter=0
    while counter<len(intervals)-1:
        if(intervals[counter][0]<= intervals[counter+1][0] and intervals[counter][1]>=intervals[counter+1][1] ):
            intervals.pop(counter+1)
            continue
        elif(intervals[counter][1]>=intervals[counter+1][0]):
            if(intervals[counter+1][0]<intervals[counter][0]):
                intervals[counter]=[intervals[counter+1][0], max(intervals[counter+1][1], intervals[counter][1])]
                intervals.pop(counter+1)
                continue
            first_cop=intervals[counter].copy()
            second_cop=intervals[counter+1].copy()
            intervals.pop(counter+1)
            intervals[counter]=[first_cop[0], second_cop[1]]
            
        else:
            counter+=1

    return(intervals)
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].'''