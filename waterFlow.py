def pacificAtlantic(heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(heights), len(heights[0])
        visited_pacific = []
        visited_atlantic = []

        pacific=[]
        atlantic=[]
        queue = []
        #start
        for row in range(m):
            pacific.append((row,0))
            atlantic.append((row,n-1))
        for column in range(n):
            pacific.append((0, column))
            atlantic.append((m-1, column))  
        
        directions = [(1,0), (-1,0),(0,1),(0,-1)]
        def dfs(row, column, visited):
            if(row, column) not in visited:
                visited.append((row,column))
            for x, y in directions:
                new_row, new_column = row+x, column + y
                if(m>new_row>=0 and n>new_column>=0 and heights[new_row][new_column] >= heights[row][column] and (new_row, new_column) not in visited):
                    dfs(new_row, new_column, visited)
        for i in pacific:
            dfs(i[0], i[1], visited_pacific)
        for i in atlantic:
            dfs(i[0], i[1], visited_atlantic)
        in_both = []
        print(visited_atlantic, "<= atlantic visited")
        print(visited_pacific, "<= pacific visited")
        for i in visited_atlantic:
            if i in visited_pacific:
                in_both.append(i)
        return in_both


print(pacificAtlantic([[2,1], [1,2]]))