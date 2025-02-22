def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    sum_total = sum1 + sum2
    if sum_total % 2 != 0:
        return -1
    target = sum_total // 2
    
    index1, index2 = 0, 0
    cnt = 0
    max_ops = 2*(len(queue1) + len(queue2))
    
    while cnt <= max_ops:
        if sum1 == target:
            return cnt
        if sum1 > target:
            if index1 < len(queue1):
                sum1 = sum1 - queue1[index1]
                sum2 = sum2 + queue1[index1]
                queue2.append(queue1[index1])
                index1 += 1
                
            '''
            sum1 = sum1 - queue1[index1%len(queue1)]
            sum2 = sum2 + queue1[index1%len(queue1)]
            queue2.append(queue1[index1%len(queue1)])
            index1 += 1
            '''
        else:
            if index2 < len(queue2):
                sum2 = sum2 - queue2[index2]
                sum1 = sum1 + queue2[index2]
                queue1.append(queue2[index2])
                index2 += 1
        cnt += 1
    return -1





#Test Cases
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2)) 