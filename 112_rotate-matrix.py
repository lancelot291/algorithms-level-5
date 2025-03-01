'''runtime error'''
import copy
def solution(rows, columns, queries):
    arr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    #print(arr)
    arrr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    # initialize the 2D array
    n = len(queries)
    result = []
    for t in range(n):
        x1, y1, x2, y2 = queries[t]
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        h, w = x2-x1, y2-y1
        rectangle = []
        # the width and height of the rectangle
        for i in range(w):
            arr[x1][y1+i+1] = arrr[x1][y1+i]
            rectangle.append(arrr[x1][y1+i])
        for i in range(h):
            arr[x1+i+1][y2] = arrr[x1+i][y2]
            rectangle.append(arrr[x1+i][y2])
        for i in range(w):
            arr[x2][y2-i-1] = arrr[x2][y2-i]
            rectangle.append(arrr[x2][y2-i])
        for i in range(h):
            arr[x2-i-1][y1] = arrr[x2-i][y1]
            rectangle.append(arrr[x2-i][y1])
        result.append(min(rectangle))
        arrr = copy.deepcopy(arr)
    return result
# Test Cases
rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))  

            
            
        
        
    

