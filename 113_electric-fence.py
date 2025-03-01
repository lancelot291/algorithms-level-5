def line(a, wires):
    set_a = set([a])
    for _ in range(len(wires)):
        for i in range(len(wires)):
            p, q = wires[i]
            if p in set_a:
                set_a.add(q)
            if q in set_a:
                set_a.add(p)
    return len(set_a)
        

def solution(n, wires):
    for i in range(n-1):
        a, b = wires[i]
        wires_2 = wires[:i] + wires[i+1:]
        abs_diff = abs(line(a, wires_2) - line(b, wires_2))
        if i == 0:
            min_diff = abs_diff
        else:
            min_diff = min(min_diff, abs_diff)
            
    return min_diff

# Test Cases
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires)) 



