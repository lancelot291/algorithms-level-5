from itertools import permutations
def is_prime(n):
    """check if the number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
    # check divisibilty upto square root of n
        if n % i == 0:
            return False
    return True

def solution(numbers):
    '''returns the number of prime numbers that can be made from the given numbers'''
    num_set = set()
    cnt = 0
    for i in range(1, len(numbers) + 1):
    # determine how many numbers we are goin to permutate
        for p in permutations(numbers, i):
        # permutate the numbers
            num = int(''.join(p))
            # make the permutated numbers into one integer
            num_set.add(num)
            # add the number to the set
    for num in num_set:
        if is_prime(num): 
        # chech if the number is prime
            cnt += 1
            #if it is prime, increment the count

    return cnt

    
    
# Test cases
numbers = "17"
print(solution(numbers))  # Output: 3