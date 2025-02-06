def solution(numbers, target):
    def recursive(numbers, target):
        if numbers: 
            return recursive(numbers[1:], target - numbers[0]) + recursive(numbers[1:], target + numbers[0]) 
        else:
            if target == 0:
                return 1
            else:
                return 0   
    return recursive(numbers, target)

print(solution([1, 1, 1, 1, 1], 3)) # 5
    