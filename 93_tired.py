def solution(k, dungeons):
    max_dungeons = 0    
    dungeons_cleared = [False] * len(dungeons)
    def explore_dungeons(hp, cnt, cleared_dungeons_order):
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, cnt)
        # print(f"current hp: {hp}, dungeons cleared: {cnt}, name of cleared dungeons: {cleared_dungeons_order}")
        
        for i in range(len(dungeons)):
            required_hp, consumption = dungeons[i]
            
            if not dungeons_cleared[i] and hp >= required_hp:
                dungeons_cleared[i] = True
                explore_dungeons(hp - consumption, cnt + 1, cleared_dungeons_order + [i])
                dungeons_cleared[i] = False # backtrack to explore dungeons in other possibilities
                
    explore_dungeons(k, 0, [])
    return max_dungeons
  
        
    
        
            
    
    