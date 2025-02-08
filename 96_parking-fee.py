def solution(fees, records):
    for i in range(len(records)):
        records[i] = records[i].split() # Split the string by space
        records[i][0] = int(records[i][0][:2])*60 + int(records[i][0][3:]) #change the time to minutes
    dict_time = {} # Create a dictionary to store the time of each car
    for record in records:
        if record[1] not in dict_time:
            dict_time[record[1]] = 0 # Initialize the time of each car to 0
    for record in records:
        if record[2] == "IN":
            dict_time[record[1]] -= record[0] # If the car is in, subtract the time when the car is in
        else:
            dict_time[record[1]] += record[0] # If the car is out, add the time when the car is out
            
    for car_number in list(dict_time.keys()):
        cnt = 0
        for record in records:
            if record[1] == car_number:
                cnt += 1
        if cnt % 2 == 1:
            dict_time[car_number] += 1439 # If the car is still in the parking lot, add the time until the end of the day
            
    # print(dict_time)
            
    for car_number in list(dict_time.keys()):
        if dict_time[car_number] <= fees[0]:
            dict_time[car_number] = fees[1]  
        elif (dict_time[car_number] - fees[0]) % fees[2] == 0:
            dict_time[car_number] = fees[1] + ((dict_time[car_number] - fees[0]) // fees[2]) * fees[3]
        else: #ceiling division
            dict_time[car_number] = fees[1] + ((dict_time[car_number] - fees[0]) // fees[2] + 1) * fees[3]
            
    answer = []
        
    for car_number in list(sorted(dict_time.keys())): # Sort the car numbers
        answer.append(dict_time[car_number])
        
    return answer
    
# Test cases
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records)) # Output: [14600, 34400, 5000]
            
    