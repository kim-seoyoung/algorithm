def floyd_warshall_1way(map_, n):    
    for i in range(n):
        for j in range(n):
            if j != i:
                for k in range(n):
                    if k != i:
                        map_[j][k] = min(map_[j][k], map_[j][i] + map_[i][k])

def solution(n, s, a, b, fares):
    inf_ = 10**6
    map_ = [[inf_ for _ in range(n)] for _ in range(n)]
    for i in range(n):
        map_[i][i] = 0
    for fare in fares:
        i, j, w = fare
        map_[i-1][j-1] = w
        map_[j-1][i-1] = w
    floyd_warshall_1way(map_, n)
    
    answer = map_[s-1][a-1] + map_[s-1][b-1]
    for i in range(n):
        answer = min(answer, map_[s-1][i] + map_[i][a-1] + map_[i][b-1])
    return answer
