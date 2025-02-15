def solution(number, k):
    '''returns the largest number that can be made by removing k digits from the number'''
    stack = []
    for digit in number:
        while stack and stack[-1] < digit and k>0:
            stack.pop()
            k-=1
        stack.append(digit)
        
    if k>0:
        stack = stack[:-k]
    return ''.join(stack)
        
# Test cases
number = "1924"
k = 2
print(solution(number, k))  # Output: 94, 92, 24