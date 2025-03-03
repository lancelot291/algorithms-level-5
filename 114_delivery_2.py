def solution(N, road, K):
    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    min_time = {i: float('inf') for i in range(1, N+1)}
    min_time[1] = 0
    visited = set()
    
    while len(visited) < N:
        current_town = 0
        current_time = float('inf')
        for town in range(1, N+1):
            if town not in visited and min_time[town] < current_time:
                current_town = town
                current_time = min_time[town]
        if current_town == 0:
            break
        visited.add(current_town)   
        for neighbor, time in graph[current_town]:
            if neighbor not in visited:
                min_time[neighbor] = min(min_time[neighbor], min_time[current_town] + time)
    return len([i for i in min_time.values() if i <= K])

# Test Cases
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))  # Expected 4
        