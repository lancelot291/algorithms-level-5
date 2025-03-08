def solution(data, col, row_begin, row_end):
    col -= 1
    row_begin -= 1
    row_end -= 1
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][col] > data[j][col]:
                data[i], data[j] = data[j], data[i]
            elif data[i][col] == data[j][col]:
                if data[i][0] < data[j][0]:
                    data[i], data[j] = data[j], data[i]
                    
    data_2 = data[row_begin:row_end+1]
    for i in range(len(data_2)):
        S_i = 0
        for j in range(len(data_2[0])):
            S_i += data_2[i][j]%(i + row_begin + 1)
        if i == 0:
            answer = S_i
        else:
            answer^=S_i
    return answer

# Test cases
data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3
print(solution(data, col, row_begin, row_end)) 