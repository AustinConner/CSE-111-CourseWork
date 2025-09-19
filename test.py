import heapq

def heuristic(a, b):
    """Calculates the Manhattan distance heuristic between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    """
    Finds the shortest path in a maze using A*.
    This version does not use classes.
    """
    # open_list is a priority queue to get the node with the lowest F-score.
    # We store tuples of (f_score, current_position).
    open_list = []
    heapq.heappush(open_list, (0, start))

    # came_from dictionary will store the path.
    # came_from[neighbor] = current
    came_from = {}

    # g_score stores the cost from start to a node.
    # Initialize all scores to infinity.
    g_score = { (r, c): float('inf') for r, row in enumerate(maze) for c, val in enumerate(row) }
    g_score[start] = 0

    # f_score is our total score (g_score + heuristic).
    # It represents our best guess of the shortest path through a node.
    f_score = { (r, c): float('inf') for r, row in enumerate(maze) for c, val in enumerate(row) }
    f_score[start] = heuristic(start, end)
    
    # Keep track of items in the open_list for faster lookups.
    open_list_hash = {start}

    while open_list:
        # Get the node in the open list with the lowest f_score.
        # The `_` is used to discard the f_score, as we only need the position.
        _, current_pos = heapq.heappop(open_list)
        open_list_hash.remove(current_pos)

        # If we've reached the end, reconstruct the path and return it.
        if current_pos == end:
            path = []
            while current_pos in came_from:
                path.append(current_pos)
                current_pos = came_from[current_pos]
            path.append(start)
            return path[::-1] # Return the reversed path

        # Check all neighbors of the current node.
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Right, Left, Down, Up
            neighbor_pos = (current_pos[0] + move[0], current_pos[1] + move[1])

            # Check if the neighbor is valid (within grid and not a wall).
            if 0 <= neighbor_pos[0] < len(maze) and 0 <= neighbor_pos[1] < len(maze[0]) and maze[neighbor_pos[0]][neighbor_pos[1]] == 0:
                
                # The distance from start to this neighbor through the current node.
                tentative_g_score = g_score[current_pos] + 1
                
                # If this path to the neighbor is better than any previous one, record it.
                if tentative_g_score < g_score[neighbor_pos]:
                    came_from[neighbor_pos] = current_pos
                    g_score[neighbor_pos] = tentative_g_score
                    f_score[neighbor_pos] = tentative_g_score + heuristic(neighbor_pos, end)
                    
                    # If neighbor is not in the open list, add it.
                    if neighbor_pos not in open_list_hash:
                        heapq.heappush(open_list, (f_score[neighbor_pos], neighbor_pos))
                        open_list_hash.add(neighbor_pos)

    # If the loop finishes and we haven't found the end, there is no path.
    return None

def main():
    # 0 represents a walkable path, 1 represents a wall.
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

    start = (0, 0)
    end = (9, 9)

    path = astar(maze, start, end)

    if path:
        print("Path found:")
        print(path)
    else:
        print("No path found")

if __name__ == '__main__':
    main()