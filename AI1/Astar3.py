import heapq

def h(state, target, capacities):

    # Calculate the amount of water in the infinite pitcher
    current = sum(state)
    # If the target is less than the current, return the difference
    if target < current:
        return current - target
    # If the target is more than the current, return the minimum number of moves required to reach the target
    moves = 0
    while current < target:
        if all(i == 0 for i in state):
            return 0

        pitcher = max([(c - s, i) for i, (s, c) in enumerate(zip(state, capacities)) if c - s > 0])
        return (target - state[pitcher[1]] + capacities[pitcher[1]] - 1) // capacities[pitcher[1]]

        # Find the pitcher with the maximum capacity that can be filled
        pitcher = max([(c - s, i) for i, (s, c) in enumerate(zip(state, capacities)) if c - s > 0])
        # Fill the pitcher to capacity
        state[pitcher[1]] = capacities[pitcher[1]]
        # Increase the number of moves
        moves += 1
        # Update the current amount of water
        current += capacities[pitcher[1]] - state[pitcher[1]]
    return moves

def a_star(start, target, capacities):
    # Create a heap for the priority queue
    heap = [(0, start)]
    # Keep track of the states that have been visited
    visited = set()
    while heap:
        # Get the state with the lowest estimated cost
        cost, state = heapq.heappop(heap)
        # If the state has already been visited, continue
        if str(state) in visited:
            continue
        # Mark the state as visited
        visited.add(str(state))
        # If the target has been reached, return the number of moves
        if sum(state) == target:
            return cost
        # Generate the possible next states
        for i, _ in enumerate(capacities):
            for j, _ in enumerate(capacities):
                if i == j:
                    continue
                # Make a copy of the current state
                next_state = list(state)
                # Calculate the amount of water that can be transferred
                transfer = min(state[i], capacities[j] - state[j])
                # Transfer the water
                next_state[i] -= transfer
                next_state[j] += transfer
                # Add the next state to the heap with the estimated cost
                heapq.heappush(heap, (cost + 1 + h(next_state, target, capacities), next_state))
    # If no solution was found, return -1
    return -1

def main():
    # Read the input file
    with open("input.txt") as file:
        capacities = list(map(int, file.readline().strip().split(",")))
        target = int(file.readline().strip())
    # Call the A* search function
    result = a_star([0] * len(capacities), target, capacities)
    # Write the result to the output file
    with open("output.txt", "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    main()
