def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = None
    
    while left < len(sequence) and right < len(sequence):
        if current_sum == k:
            if best_range is None or (best_range[1] - best_range[0]) > (right - left):
                # if the current best_range is shorter than the previous best_range
                best_range = (left, right)
            elif (best_range[1] - best_range[0]) == (right - left) and best_range[0] > left:
                # if the current best_range is the same length as the previous best_range
                # but the current best_range starts later
                best_range = (left, right)
        if current_sum>=k:
            current_sum-=sequence[left]
            left+=1
        elif current_sum<k:
            right+=1
            if right<len(sequence):
                current_sum+=sequence[right]
            
    return [best_range[0], best_range[1]]

# Test cases
sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))  # Output: [2, 3]
    
    