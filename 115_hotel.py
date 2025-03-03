def time_to_min(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])
def solution(book_time):
    events = []
    for start, end in book_time:
        events.append((time_to_min(start), 1))
        events.append((time_to_min(end)+10, -1))
    events.sort()
        
    #print(events)
        
    max_rooms = 0
    rooms = 0
    for _, delta in events:
        rooms += delta
        max_rooms = max(max_rooms, rooms)
            
    return max_rooms

# Test Cases
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))  
    

        

    