def time_to_min(time):
    time = time.split(':')
    return int(time[:2]) * 60 + int(time[2:])
def solution(book_time):
    for start, end in book_time:
        start = time_to_min(start)
        end = time_to_min(end)
        

    