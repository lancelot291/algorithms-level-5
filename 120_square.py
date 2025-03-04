def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solution(w,h):
    return w*h - (w+h-gcd(w,h))
# Test Cases
w = 8
h = 12
print(solution(w,h)) # 80
    