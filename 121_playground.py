def solution(weights):
    answer = 0
    weight_frequqncy = {}
    for weight in weights:
        if weight in weight_frequqncy:
            weight_frequqncy[weight] += 1
        else:
            weight_frequqncy[weight] = 1
    for weight in weight_frequqncy:
        answer += weight_frequqncy[weight] * (weight_frequqncy[weight]-1) / 2
    for weight in weight_frequqncy:
        for ratio in [2, 4/3, 3/2]:
            if weight * ratio in weight_frequqncy:
                answer += weight_frequqncy[weight] * weight_frequqncy[weight*ratio]
    return int(answer)

# Test cases
print(solution([100,180,360,100,270])) # 6