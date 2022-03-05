def solution():
    V, E = input().split()
    V = int(V)
    E = int(E)

    edges = []
    for _ in range(E):
        in_ = list(map(int, input().split()))
        edges.append(in_)

    inf_ = 100000000
    dist = [inf_ for _ in range(V+1)]
    
    dist[1] = 0
    isOK = True
    for i in range(V):
        for edge in edges:
            s,e,v = edge

            if dist[s] != inf_ and dist[e] > dist[s] + v:
                dist[e] = dist[s] + v
                if i == V-1:
                    isOK = False

    if isOK:
        for i in range(2, V+1):
            if dist[i] == inf_:
                print(-1)
            else:
                print(dist[i])
    else:
        print(-1)

    

solution()
