import math
import random

def objective(x):
    return (x - 3) ** 2

def generate_neighbour(x):
    return x + random.uniform(-1, 1)

def simulated_annealing(initial_state, initial_temperature, cooling_rate, minimum_temperature, maximum_iterations, seed):
    random.seed(seed)
    
    current_state = initial_state
    current_cost = objective(current_state)
    best_state = current_state
    best_cost = current_cost
    temperature = initial_temperature
    
    for iteration in range(1, maximum_iterations + 1):
        if temperature <= minimum_temperature:
            break
            
        candidate_state = generate_neighbour(current_state)
        candidate_cost = objective(candidate_state)
        delta = candidate_cost - current_cost
        
        accepted = False
        if delta < 0:
            accepted = True
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                accepted = True
                
        if accepted:
            current_state = candidate_state
            current_cost = candidate_cost
            
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost
                
        temperature *= cooling_rate
        
    return best_state, best_cost

print("----------------")
print("---Test Cases---")
print("----------------")

print("Test Case 1: Initial State at the Optimum")
best_x, min_val = simulated_annealing(
    initial_state=3,
    initial_temperature=100,
    cooling_rate=0.95,
    minimum_temperature=0.01,
    maximum_iterations=500,
    seed=1
)
print(f"Best State (x): {best_x:.6f}")
print(f"Minimum Function Value: {min_val:.8f}\n")

print("Test Case 2: Initial State Below the Optimum")
best_x, min_val = simulated_annealing(
    initial_state=-5,
    initial_temperature=100,
    cooling_rate=0.95,
    minimum_temperature=0.01,
    maximum_iterations=500,
    seed=42
)
print(f"Best State (x): {best_x:.6f}")
print(f"Minimum Function Value: {min_val:.8f}\n")

print("Test Case 3: Initial State Above the Optimum")
best_x, min_val = simulated_annealing(
    initial_state=9,
    initial_temperature=100,
    cooling_rate=0.95,
    minimum_temperature=0.01,
    maximum_iterations=500,
    seed=7
)
print(f"Best State (x): {best_x:.6f}")
print(f"Minimum Function Value: {min_val:.8f}\n")

print("Test Case 4: Low Initial Temperature")
best_x, min_val = simulated_annealing(
    initial_state=0,
    initial_temperature=1,
    cooling_rate=0.9,
    minimum_temperature=0.01,
    maximum_iterations=500,
    seed=10
)
print(f"Best State (x): {best_x:.6f}")
print(f"Minimum Function Value: {min_val:.8f}\n")

print("Test Case 5: Fast Cooling Schedule")
best_x, min_val = simulated_annealing(
    initial_state=10,
    initial_temperature=100,
    cooling_rate=0.5,
    minimum_temperature=0.01,
    maximum_iterations=100,
    seed=21
)
print(f"Best State (x): {best_x:.6f}")
print(f"Minimum Function Value: {min_val:.8f}\n")
