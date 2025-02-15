def same(arr,x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                return False
    return True

def solution(arr):
    n = len(arr)
    answer = [0, 0]
    def compress(x, y, n):
        if same(arr, x, y, n):
            answer[arr[x][y]] += 1
        else:
            m = n // 2
            compress(x, y, m)
            compress(x, y+m, m)
            compress(x+m, y, m)
            compress(x+m, y+m, m)
    compress(0, 0, n)
    return answer
    
# Test cases
arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
print(solution(arr))  # Output: [4, 9]