class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if (row, col) in visited:
                return False
            else:
                visited.add((row, col))

                if (row + 1) <= rows- 1 and grid[row + 1][col] == "1":
                    dfs(row + 1, col)
                if (row - 1) >= 0 and grid[row - 1][col] == "1":
                    dfs(row - 1, col)
                if (col + 1) <= cols - 1 and grid[row][col + 1] == "1":
                    dfs(row, col + 1)
                if (col - 1) >= 0 and grid[row][col - 1] == "1":
                    dfs(row, col - 1)
            
            return True


        for row in range(rows): 
            for col in range(cols):
                current = grid[row][col]

                if current == "1":
                    if dfs(row, col): 
                        count += 1
        
        return count