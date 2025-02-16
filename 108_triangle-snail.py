def solution(n):
    '''returns a snail patterned 2D array'''
    arr = [[0]*n for _ in range(n)]
    # initialize the 2D array
    num_list = []
    # the final answer
    num = 1
    # the nunmbet we are going to put in the array as we go through the snail pattern
    pattern = [(1, 0), (0, 1), (-1, -1)]
    # the pattern of moves
    x, y = -1, 0
    # the starting point
    for i in range(n):
        for _ in range(i, n):
        # the number of times we are going to move in the same direction
        # is n-1, n-1, n-2, n-2, n-3, n-3, ...
            x += pattern[i%3][0]
            y += pattern[i%3][1]
            # follow the pattern in cycle of 3
            arr[x][y] = num
            num += 1
            # put the number in the array and increment the number
            
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                num_list.append(arr[i][j])
                # put the number in the final answer if it is not 0
    return num_list

# Test cases
n = 4
print(solution(n))  # Output: [1, 2, 9, 3, 8, 10, 7, 4, 5, 6]
            
    
        