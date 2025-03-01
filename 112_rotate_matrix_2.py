def solution(rows, columns, queries):
    arr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    min_vals = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        min_val = arr[x1][y1]
        tmp = arr[x1][y1]
        for i in range(x1, x2):
            min_val = min(min_val, arr[i][y1])
            arr[i][y1] = arr[i+1][y1]
        for i in range(y1, y2):
            min_val = min(min_val, arr[x2][i])
            arr[x2][i] = arr[x2][i+1]
        for i in range(x2, x1, -1):
            min_val = min(min_val, arr[i][y2])
            arr[i][y2] = arr[i-1][y2]
        for i in range(y2, y1, -1):
            min_val = min(min_val, arr[x1][i])
            arr[x1][i] = arr[x1][i-1]
        arr[x1][y1+1] = tmp
        min_vals.append(min_val)
        
    return min_vals

# Test Cases
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))  # Output: [8, 10, 25]
        