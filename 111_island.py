def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # A 2D list to keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]
    
    # Direction vectors for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]