import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)



def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):

        if tile != 0:
            goal_index = GOAL.index(tile)

            row = i // 3
            col = i % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(row - goal_row)
            distance += abs(col - goal_col)

    return distance



def successors(state):

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    result = []

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            result.append((tuple(new_state), move))

    return result



def astar(start):

    frontier = []

    g = 0
    f = g + heuristic(start)

    heapq.heappush(
        frontier,
        (f, g, start, [])
    )

    explored = set()

    while frontier:

        f, g, state, path = heapq.heappop(frontier)

        if state == GOAL:
            return path

        if state in explored:
            continue

        explored.add(state)

        for child, move in successors(state):

            if child not in explored:

                new_g = g + 1
                new_f = new_g + heuristic(child)

                new_path = path + [(move, child)]

                heapq.heappush(
                    frontier,
                    (new_f, new_g, child, new_path)
                )

    return None



def print_puzzle(state):

    for i in range(0, 9, 3):

        row = []

        for j in range(i, i + 3):

            if state[j] == 0:
                row.append("_")
            else:
                row.append(str(state[j]))

        print(" ".join(row))

    print()



test_cases = [

    (
        1, 2, 3,
        4, 5, 6,
        7, 0, 8
    ),

    (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    ),

    (
        1, 2, 3,
        0, 5, 6,
        4, 7, 8
    )
]




for number, start in enumerate(test_cases, 1):

    print("================================")
    print("Test Case:", number)
    print("================================")

    print("Input:")
    print_puzzle(start)

    solution = astar(start)

    if solution is not None:

        print("Solution Found")
        print()

        for i, (move, state) in enumerate(solution, 1):

            print("Move", i, ":", move)
            print_puzzle(state)

        print("Goal State Reached")
        print("Solution Cost =", len(solution))

    else:

        print("No solution")

    print()
