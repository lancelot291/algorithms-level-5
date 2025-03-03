def solution(places):
# Directions for checking adjacent and diagonal positions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    two_space_moves = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    result = []
    for room in places:
        val = 1
        for i in range(5):
            for j in range(5) :
                if room[i][j] == 'P':
                    for direction in directions:
                        x, y = i + direction[0], j + direction[1]
                        if 0 <= x < 5 and 0 <= y < 5 and room[x][y] == 'P':
                            val = 0
                    for diagonal in diagonals:
                        x, y = i + diagonal[0], j + diagonal[1]
                        if 0 <= x < 5 and 0 <= y < 5 and room[x][y] == 'P':
                            if room[i + diagonal[0]][j] != 'X' or room[i][j + diagonal[1]] != 'X':
                                val = 0
                    for two_space_move in two_space_moves:
                        x, y = i + two_space_move[0], j + two_space_move[1]
                        if 0 <= x < 5 and 0 <= y < 5 and room[x][y] == 'P':
                            if room[i + two_space_move[0]//2][j + two_space_move[1]//2] != 'X':
                                val = 0
        result.append(val)
        
    return result

# Test Cases
places  = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))  # Expected [1, 0, 1, 1, 1]
    
    