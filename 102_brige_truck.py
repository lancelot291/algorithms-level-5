def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length  # Bridge initialized with zeros
    current_weight = 0  # Track the weight of trucks currently on the bridge

    while bridge or truck_weights:  # Ensure trucks keep moving until all are processed
        time += 1  # Increment time each step
        left_truck = bridge.pop(0)  # Truck leaves the bridge
        current_weight -= left_truck  # Subtract its weight from the current load

        if truck_weights:
            # Check if the next truck can enter the bridge
            if current_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.pop(0)  # Take next truck
                bridge.append(next_truck)  # Put it on the bridge
                current_weight += next_truck  # Update bridge weight
            else:
                bridge.append(0)  # No truck enters, just move time forward

    return time

# Test cases
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))  # Output: 8
