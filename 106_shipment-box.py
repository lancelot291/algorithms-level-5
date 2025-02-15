

def solution(order):
    stack = []
    index = 0
    belt = list(range(1, len(order) + 1))
    cnt = 0
    for box in order:
        while index<len(belt) and (not stack or stack[-1] != box):
            stack.append(belt[index])
            index+=1
        if stack and stack[-1] == box:
            stack.pop()
            cnt += 1
        else :
            break
    return cnt

            
        
 

# Test cases
order = [4, 3, 1, 2, 5]
print(solution(order))  # Output: 2