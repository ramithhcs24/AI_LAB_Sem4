from queue import PriorityQueue

def A_star(graph, heuristic, start, goal):
    if start not in graph or start not in heuristic:
        print("No path exists")
        return
        
    g = {}
    f = {}
    
    pq = PriorityQueue()
    g[start] = 0
    f[start] = heuristic[start]
    
    pq.put((f[start], start))
    
    parent = {start: None}  
    
    while not pq.empty():
        current_f, current = pq.get()
        
        if current == goal:
            path = []
            temp = current
            while temp is not None:
                path.append(temp)
                temp = parent[temp]
            path.reverse()  
            
            print("Path found:", " -> ".join(map(str, path)))
            print("Total cost:", g[goal])
            return
            
        if current_f > f.get(current, float('inf')):
            continue
            
        if current not in graph:
            continue
            
        for neighbour, edge_cost in graph[current].items():
            tentative_g = g[current] + edge_cost
            if neighbour not in g or tentative_g < g[neighbour]:
                parent[neighbour] = current
                g[neighbour] = tentative_g
                f[neighbour] = g[neighbour] + heuristic.get(neighbour, 0)
                pq.put((f[neighbour], neighbour))
                
    print("No path exists")

graph={
    'A': {'B': 1, 'C': 2,'H': 7},
    'B': {'D': 4, 'E': 6},
    'C': {'F': 3, 'G': 2},
    'D': {'E': 7},
    'E': {},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}
heuristic={
    'A': 5,'B': 3,'C': 4,'D' :2,
    'E' :6,'F': 3,'G': 1,'H': 0
}
print("Ramith H 1WN24CS222")

print("----------------")
print("---Test Cases---")
print("----------------")

print("Test Case 1")
A_star(graph,heuristic,'A','H')

print("Test Case 2")
A_star(graph,heuristic,'A','A')

print("Test Case 3")
A_star(graph,heuristic,'A','D')

print("Test Case 4")
A_star(graph,heuristic,'A','F')

print("Test Case 5")
A_star(graph,heuristic,'A','Z')

print("Test Case 7")
A_star(graph,heuristic,'A','H')

print("Test Case 8")
A_star(graph,heuristic,'X','H')

g1={
    'A': {'B': 2},
    'B': {'A': 2},
    'C': {}
}
h1={
    'A': 2,
    'B': 1,
    'C': 0
}

print("Test Case 6")
A_star(g1,h1,'A','C')
