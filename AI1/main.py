import heapq

def get_children(state, capacities):
    children = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i == j:
                continue
            temp = state[:]
            if temp[i] + temp[j] <= capacities[j]:
                temp[j] += temp[i]
                temp[i] = 0
            else:
                temp[i] -= capacities[j] - temp[j]
                temp[j] = capacities[j]
            children.append(temp)
    return children

def astar(capacities, target):
    start = [0 for _ in capacities]
    heap = [(0, 0, start)]
    visited = set()
    while heap:
        (steps, cost, state) = heapq.heappop(heap)
        if sum(state) == target:
            return steps
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        children = get_children(state, capacities)
        for child in children:
            priority = cost + abs(sum(child) - target) + 1
            heapq.heappush(heap, (steps + 1, priority, child))
    return -1

def main():
    capacities = []
    target = 0
    with open("input.txt") as f:
        capacities = list(map(int, f.readline().strip().split(",")))
        target = int(f.readline().strip())
    result = astar(capacities, target)
    print(result)

if __name__ == "__main__":
    main()