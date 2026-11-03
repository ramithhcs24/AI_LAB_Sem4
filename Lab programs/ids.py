CUTOFF = "cutoff"
FAILURE = "failure"

def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]
    
    if limit == 0:
        return CUTOFF
    
    cutoff_occurred = False
    
    children = graph.get(node, [])
    
    for child in children:
        if child not in path:
            result = depth_limited_search(child, goal, graph, limit - 1, path + [node])
            
            if result != CUTOFF and result != FAILURE:
                return result
            
            if result == CUTOFF:
                cutoff_occurred = True
                
    if cutoff_occurred:
        return CUTOFF
    else:
        return FAILURE

def iterative_deepening_search(initial, goal, graph, maximum_depth):
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, [])
        
        if result != CUTOFF and result != FAILURE:
            return f"Solution found at depth {depth}: {result}"
            
    return "Failure: Goal not found within maximum depth."


print("--- Running Iterative Deepening Search Test Cases ---")

graph1 = {
    'A': ['B', 'C'],
    'B': [],
    'C': []
}
print("\nTest Case 1: Goal at Depth 1")
print(iterative_deepening_search(initial='A', goal='B', graph=graph1, maximum_depth=3))


graph2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
print("\nTest Case 2: Goal at Depth 2")
print(iterative_deepening_search(initial='A', goal='G', graph=graph2, maximum_depth=3))


graph3 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [], 'E': []
}
print("\nTest Case 3: Goal Not Present")
print(iterative_deepening_search(initial='A', goal='Z', graph=graph3, maximum_depth=2))


graph4 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
print("\nTest Case 4: Goal at Maximum Depth (2)")
print(iterative_deepening_search(initial='A', goal='G', graph=graph4, maximum_depth=2))

graph5 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [], 'E': []
}
print("\nTest Case 5: Goal Not Present (Additional)")
print(iterative_deepening_search(initial='A', goal='Z', graph=graph5, maximum_depth=2))
