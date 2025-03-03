def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solution(arrayA, arrayB):
    #print(arrayA, arrayB)
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
    for i in range(1, len(arrayB)):   
        gcd_b = gcd(gcd_b, arrayB[i])
    array_A = sorted(list(filter(lambda x: gcd_a % x == 0, [i for i in range(1, gcd_a+1)])), reverse=True)
    array_B = sorted(list(filter(lambda x: gcd_b % x == 0, [i for i in range(1, gcd_b+1)])), reverse=True)
    #print(array_A, array_B)
    
    num_a = 0
    for a in array_A:
        for b in arrayB:
            if b%a == 0:
                a = 0
                break
        if a != 0:
            num_a = a 
        break
        
    num_b = 0
    for b in array_B:
        for a in arrayA:
            if a%b == 0:
                b = 0
                break
        if b != 0:
            num_b = b
        break
        
    return max(num_a, num_b) 

# Test Cases
arrayA = [10,17]
arrayB = [5, 20]
print(solution(arrayA, arrayB)) 
        

    