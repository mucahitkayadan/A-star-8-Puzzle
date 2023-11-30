# 8-Puzzle Solver

This is a Python program that solves the 8-puzzle using the A* algorithm with the Manhattan Distance heuristic.

## Description

The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to arrange the tiles in ascending order, starting from the top-left corner.

This program uses the A* algorithm to find the optimal solution to the 8-puzzle problem. The A* algorithm combines the cost to reach a node (g) and the estimated cost to the goal (h) to determine the best path.

The Manhattan Distance heuristic is used to estimate the cost from each state to the goal state. It calculates the sum of the distances between each tile and its goal position.

## Usage

To use this program, follow these steps:

1. Install Python (version 3.6 or higher) if you haven't already.
2. Open the `main.py` file in a Python IDE or text editor.
3. Modify the `initial_state_1` and `initial_state_2` variables to define your own puzzle problems.
4. Run the program.
5. The program will output the solutions to the puzzle problems, if found.

## Example Problems

The program includes two example problems:

1. Problem 1: Initial state `[1, 2, 3], [4, 5, 6], [0, 7, 8]`
   - Solution: `[1, 2, 3], [4, 5, 6], [7, 8, 0]`

2. Problem 2: Initial state `[2, 8, 1], [0, 4, 3], [7, 6, 5]`
   - Solution: `No solution found for problem 2.`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.