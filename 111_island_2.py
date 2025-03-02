def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    # A 2D list to keep track of visited cells
    visited = [[0] * cols for _ in range(rows)]
    
    # Direction vectors for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(r, c):
        total = 0
        stack = [(r, c)]
        while stack:
            cur_r, cur_c = stack.pop()
            if visited[cur_r][cur_c]:
                continue
            visited[cur_r][cur_c] = 1
            total += int(maps[cur_r][cur_c])
            
            for dx, dy in directions:
                new_r, new_c = cur_r + dx, cur_c + dy
                if 0<=new_r<rows and 0<=new_c<cols and not visited[new_r][new_c] and maps[new_r][new_c] != 'X':
                    stack.append((new_r, new_c))
        
        
        
        return total
    
    islands = []
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                sum = dfs(i, j)
                islands.append(sum)
                
    return sorted(islands) if islands else [-1]

# Test Cases
maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))  
        