'''
def k_nary(n, k):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = n//k, n%k
        nums.append(str(r))
    return ''.join(reversed(nums))
    '''

def k_nary(n, k):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % k) + result
        n = n//k
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    nk = k_nary(n, k)
    nk_list = nk.split('0')
    print(nk_list)
    count = 0
    
    for num in nk_list:
        if is_prime(int(num)):
            count += 1
            
    return count

print(solution(437674, 3)) # 3
    
    
    