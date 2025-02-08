def solution(topping):
    cnt = 0
    left_toppings = set()
    right_toppings = {}
    
    for n in topping:
        if n in right_toppings:
            right_toppings[n] += 1
        else:
            right_toppings[n] = 1
    for i in range(len(topping)):
        left_toppings.add(topping[i])
        right_toppings[topping[i]] -= 1
        if right_toppings[topping[i]] == 0:
            right_toppings.pop(topping[i])
        if len(left_toppings) == len(right_toppings):
            cnt += 1
    return cnt

# Test cases
topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping)) # Output: 3