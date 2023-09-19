def solution(players, callings):
    index_map = {name: idx for idx, name in enumerate(players)}
    
    for name in callings:
        C = index_map[name]
        players[C-1], players[C] = players[C], players[C-1]

        index_map[players[C]] = C
        index_map[players[C-1]] = C - 1
    
    return players