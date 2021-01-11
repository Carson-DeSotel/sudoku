# Sudoku

A Sudoku library written in Python. 

## Algorithm: 
  - Import a 2D array representing the board
  - Note which cells are already filled. These are immutable.
  - For each empty cell (denoted as 0), find a set of possible solutions
  - Try a solution (or start with the smallest set of solutions)
    - then try every other solution for that initial solution
      - ? Recursive ?
  - Come to a valid solution