def solution(storey):
    cnt = 0
    while storey>0:
        r = storey%10
        if r>=6:
            cnt+=(10-r)
            storey+=10-r
            storey//=10
        elif r<=4:
            cnt+=r
            storey//=10
        else :
            if (storey//10)%10>=5:
                storey+=10-r
            cnt+=r
            storey//=10
            
    return cnt
