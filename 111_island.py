from collections import deque
def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # A 2D list to keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]
    
    # Direction vectors for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def bfs(r, c):
        """Performs BFS to find connected components (islands) and their food values."""
        queue = deque([(r, c)])  # Use deque for BFS
        total = 0  # Track total food in the island
        
        while queue:
            cur_r, cur_c = queue.popleft()  # Pop from the left for BFS
            
            if visited[cur_r][cur_c]:  # Skip if already visited
                continue
            
            # Mark the cell as visited
            visited[cur_r][cur_c] = True
            # Add the cell's food value to the total
            total += int(maps[cur_r][cur_c])
            
            # Check all adjacent cells
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maps[nr][nc] != 'X':
                    queue.append((nr, nc))  # Add to queue for further exploration
        
        return total
    
    islands = []  # List to store the food values of all islands
    
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                sum = bfs(i, j)
                islands.append(sum)
    return sorted(islands) if islands else [-1]
                