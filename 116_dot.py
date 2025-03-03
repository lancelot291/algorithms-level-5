import math
def solution(k, d):
    cnt = 0
    for x in range(0, d+1, k):
        cnt+=(math.floor(math.sqrt(d**2 - x**2)))//k + 1
            
    return cnt

# Test Cases
k = 1
d = 5
print(solution(k, d))  # Expected 9