def solution(N, road, K):
    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    min_time = {i: float('inf') for i in range(1, N+1)}
    min_time[1] = 0
    visited = set()
    current_town = 1
    while len(visited) < N:
        for neighbor, time in graph[current_town]:
            tmp_town = current_town
            if neighbor not in visited:
                min_time[neighbor] = min(min_time[neighbor], min_time[current_town] + time)
                visited.add(current_town)
                if min_time[neighbor] < min_time[tmp_town]:
                    tmp_town = neighbor
        current_town = tmp_town
        
    return len([i for i in min_time.values() if i <= K])

# Test Cases
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))  # Expected 4
'''
    while len(visited) < N:
        # Step 3: Find the unvisited town with the smallest delivery time
        current_town = -1
        current_time = float('inf')

        for town in range(1, N+1):
            if town not in visited and min_time[town] < current_time:
                current_town = town
                current_time = min_time[town]

        if current_town == -1:  # No more towns to visit
            break

        # Step 4: Mark the current town as visited
        visited.add(current_town)

        # Step 5: Update shortest path for neighbors
        for neighbor, time in graph[current_town]:
            if neighbor not in visited:
                min_time[neighbor] = min(min_time[neighbor], min_time[current_town] + time)

    # Step 6: Count towns where delivery time is <= K
    return len([time for time in min_time.values() if time <= K])
        
'''
    
    
    
    
    