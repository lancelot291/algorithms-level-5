def solution_3(numbers): #wrong
    
    first = 0
    first_str = ''
    
    if len(numbers) == 1:
        return str(numbers[0])
    
    for i , number in enumerate(numbers): 
        number_str = str(number) 
        # convert the number to a string
        if i == 0:
            first= int(number_str[0])
            first_str = number_str
            # set the first digit of the first number as the highest
        if first < int(number_str[0]):   
            # check if the first digit of the current number is higher than the highest
            first = int(number_str[0])   
            # set the first digit of the current number as the highest
            first_str = number_str 
            print(f'first_str:{first_str}')     
            # set the current number as the number with the highest first digit
    numbers.remove(int(first_str))
    return first_str + solution(numbers)   
    # return the number with the highest first digit and call the function recursively with the remaining numbers




def solution_2(numbers): #wrong
    if not numbers:  # Base case: If numbers list is empty, return an empty string
        return ""
    
    first = 0
    first_str = '0'  # Initialize with '0' instead of '2' to avoid incorrect comparisons

    for i, number in enumerate(numbers): 
        number_str = str(number)  # Convert the number to a string
        if i == 0 or int(number_str[0]) > first:  
            # If it's the first number OR has a higher first digit, update
            first = int(number_str[0])
            first_str = number_str  

    numbers.remove(int(first_str))  # Remove the selected number from the list
    return first_str + solution_2(numbers)  # Recursively process the remaining numbers

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    
    answer = "".join(str_numbers)
    return answer if int(answer) != 0 else "0"
    
    
    


# Test cases
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))  # Output: "6210"