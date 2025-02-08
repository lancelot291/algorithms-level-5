def solution(numbers):
    n = len(numbers)
    stack = []
    result = [-1] * n
    
    for i in range(n):
            while stack and numbers[stack[-1]] < numbers[i]:
                result[stack.pop()] = numbers[i]
            stack.append(i)
            
    return result   
        

# Test cases
numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers)) # Output: [-1, 5, 6, 6, -1, -1]
            