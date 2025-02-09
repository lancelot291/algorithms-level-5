def diff(a, b):
    cnt = 0
    a = str(a)  
    b = str(b)
    M = max(len(a), len(b))
    a = '0' * (M - len(a)) + a
    b = '0' * (M - len(b)) + b
    for i in range(M):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def solution(numbers):
    result = []
    for number in numbers:
        number_bin = bin(number)[2:]
        number_copy = number + 1
        # we will plus number_copy for 1 at a time and maintain number as it is
        while True:
            number_copy_bin = bin(number_copy)[2:]
            #print(diff(number_bin, number_copy_bin))
            if diff(number_bin, number_copy_bin) <= 2:
            # if the difference between the binary representation of number and number_copy 
            # is less than or equal to 2
                result.append(number_copy)
                break
            number_copy += 1
    return result


def solution(numbers):
    answer = []
    for number in numbers:
        xor_value = number ^ (number + 1)
        adjustments = xor_value >> 2
        result = number + adjustments + 1
        answer.append(result)
    return answer
        
        

# Test cases
numbers = [2, 7]
print(solution_2(numbers)) # Output: [4, 11]
            
            