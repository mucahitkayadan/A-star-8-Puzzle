import heapq
import numpy as np

# Define the goal state
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# Define the Manhattan Distance heuristic function


def manhattan_distance(state):
    """
    Calculates the Manhattan Distance heuristic for a given state.
    The Manhattan Distance is the sum of the distances between each tile and its goal position.
    Args:
        state (numpy.ndarray): The current state of the puzzle.
    Returns:
        int: The Manhattan Distance heuristic value.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_position = np.where(goal_state == state[i][j])
                distance += abs(i - goal_position[0][0]) + abs(j - goal_position[1][0])
    return distance

# Define the Node class


class Node:
    """
    Represents a node in the search tree.
    Each node contains a state, a reference to its parent node, and the cost values g and h.
    """
    def __init__(self, state, parent=None, g=0, h=0):
        """
        Initializes a new Node object.
        Args:
            state (numpy.ndarray): The state of the puzzle.
            parent (Node, optional): The parent node. Defaults to None.
            g (int, optional): The cost from the initial state to the current node. Defaults to 0.
            h (int, optional): The heuristic value of the current node. Defaults to 0.
        """
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def __lt__(self, other):
        """
        Compares two nodes based on their f values (g + h).
        This is used for the priority queue in the A* algorithm.
        Args:
            other (Node): The other node to compare with.
        Returns:
            bool: True if the current node has a lower f value, False otherwise.
        """
        return (self.g + self.h) < (other.g + other.h)

# Define the A* algorithm function


def solve_8_puzzle(initial_state):
    """
    Solves the 8-puzzle using the A* algorithm.
    Args:
        initial_state (numpy.ndarray): The initial state of the puzzle.
    Returns:
        Node or None: The goal node if a solution is found, None otherwise.
    """
    open_list = []
    closed_list = set()

    # Create the initial node
    initial_node = Node(initial_state, None, 0, manhattan_distance(initial_state))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(tuple(map(tuple, current_node.state)))

        # Check if the current node is the goal state
        if np.array_equal(current_node.state, goal_state):
            return current_node

        # Generate the next possible moves
        zero_position = np.where(current_node.state == 0)
        possible_moves = [(zero_position[0][0] - 1, zero_position[1][0]),  # Up
                          (zero_position[0][0] + 1, zero_position[1][0]),  # Down
                          (zero_position[0][0], zero_position[1][0] - 1),  # Left
                          (zero_position[0][0], zero_position[1][0] + 1)]  # Right

        for move in possible_moves:
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                new_state = np.copy(current_node.state)
                new_state[zero_position[0][0]][zero_position[1][0]] = new_state[move[0]][move[1]]
                new_state[move[0]][move[1]] = 0

                if tuple(map(tuple, new_state)) not in closed_list:
                    new_node = Node(new_state, current_node, current_node.g + 1, manhattan_distance(new_state))
                    heapq.heappush(open_list, new_node)

    return None

# Example problem 1


initial_state_1 = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
solution_1 = solve_8_puzzle(initial_state_1)

# Example problem 2
initial_state_2 = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
solution_2 = solve_8_puzzle(initial_state_2)

# Print the solutions
if solution_1:
    print("Solution 1:")
    node = solution_1
    while node:
        print(node.state)
        node = node.parent
else:
    print("No solution found for problem 1.")

print()

if solution_2:
    print("Solution 2:")
    node = solution_2
    while node:
        print(node.state)
        node = node.parent
else:
    print("No solution found for problem 2.")
