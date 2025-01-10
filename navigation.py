import heapq

def calculate_path(start, end):
    # Simulated grid for demonstration purposes
    grid = [[0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 0, 0]]
    
    # Dijkstra's algorithm for pathfinding
    def dijkstra(grid, start, end):
        queue = [(0, start)]
        distances = {start: 0}
        previous = {start: None}
        
        while queue:
            (cost, current) = heapq.heappop(queue)
            if current == end:
                break
            for neighbor in get_neighbors(current):
                new_cost = cost + grid[neighbor[0]][neighbor[1]]
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    previous[neighbor] = current
                    heapq.heappush(queue, (new_cost, neighbor))
        return reconstruct_path(previous, start, end)

    def get_neighbors(current):
        return [(current[0] + 1, current[1]), (current[0], current[1] + 1)]

    def reconstruct_path(previous, start, end):
        path = []
        current = end
        while current != start:
            path.insert(0, current)
            current = previous[current]
        return path

    return dijkstra(grid, start, end)
