class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height)
        area=0
        l,r=0, width-1
        #go in from left and right to get the largest possible area.
        # move left and right index's based on which is higher
        while l<r:
            if( height[l]< height[r] ):
                area=max(area, (r-l)*height[l])
                l+=1
            elif(height[l]>=height[r]):
                area=max(area, (r-l)*height[r])
                r-=1
        return(area)

                