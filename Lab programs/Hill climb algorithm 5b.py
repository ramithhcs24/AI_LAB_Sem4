def hill_climbing(graph, values, initial_state):
    if initial_state not in values:
        print("Invalid initial state")
        return

    current = initial_state
    
    while current in graph and graph[current]:
        best_neighbour = current
        
        for neighbour in graph[current]:
            if neighbour in values and values[neighbour] > values[best_neighbour]:
                best_neighbour = neighbour
                
        if best_neighbour == current:
            break
        else:
            current = best_neighbour
            
    print(f"Final state: {current}")
    print(f"Value: {values[current]}")

print("----------------")
print("---Test Cases---")
print("----------------")

print("Test Case 1")
graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
values1 = {
    'A': 2, 'B': 4, 'C': 5,
    'D': 7, 'E': 6, 'F': 8, 'G': 9
}
hill_climbing(graph1, values1, 'A')

print("\nTest Case 2")
graph2 = {
    'A': ['B', 'C'],
    'B': [],
    'C': []
}
values2 = {'A': 10, 'B': 5, 'C': 7}
hill_climbing(graph2, values2, 'A')

print("\nTest Case 3")
graph3 = {
    'A': ['B'],
    'B': []
}
values3 = {'A': 3, 'B': 8}
hill_climbing(graph3, values3, 'A')

print("\nTest Case 4")
graph4 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
values4 = {'A': 3, 'B': 8, 'C': 5, 'D': 6, 'E': 10}
hill_climbing(graph4, values4, 'A')

print("\nTest Case 5")
graph5 = {
    'A': ['B', 'C'],
    'B': [],
    'C': []
}
values5 = {'A': 5, 'B': 5, 'C': 5}
hill_climbing(graph5, values5, 'A')

print("\nTest Case 6")
graph6 = {
    'A': ['B', 'C'],
    'B': [],
    'C': []
}
values6 = {'A': 9, 'B': 6, 'C': 4}
hill_climbing(graph6, values6, 'A')

print("\nTest Case 7")
graph7 = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': [],
    'D': []
}
values7 = {'A': 2, 'B': 5, 'C': 9, 'D': 7}
hill_climbing(graph7, values7, 'A')

print("\nTest Case 8")
graph8 = {'A': []}
values8 = {'A': 5}
hill_climbing(graph8, values8, 'A')

print("\nTest Case 9")
graph9 = {
    'A': ['B'],
    'B': []
}
values9 = {'A': 3, 'B': 8}
hill_climbing(graph9, values9, 'X')

print("\nTest Case 10")
graph10 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
values10 = {'A': 2, 'B': 8, 'C': 4, 'D': 6, 'E': 10}
hill_climbing(graph10, values10, 'A')
