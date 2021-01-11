from board import Board 
from board import _SIZE
import math 
def _solver(x):
  x.pretty_print()
  x.generate_possibilities() # don't forget: needs to be seeded
  
  # remove 1 element sets
  for i in range(x.size):
    for j in range(x.size):
      if len(x.board[i][j].guess) == 1:
        t = x.board[i][j].guess.pop()
        x.board[i][j].value = t
        x.board[i][j].is_clue = True
        x.regenerate_possibilities(t, math.floor(i / 3), math.floor(j / 3))
  
  x.generate_possibilities()

  for i in range(x.size):
    for j in range(x.size):
      if len(x.board[i][j].guess) == 1:
        t = x.board[i][j].guess.pop()
        x.board[i][j].value = t
        x.board[i][j].is_clue = True
        x.regenerate_possibilities(t, math.floor(i / 3), math.floor(j / 3))


  print(x.board[6][1].guess, x.board[6][1].value, x.board[6][1].is_clue)
  x.pretty_print()


def solve(filename):
  x = Board(9)
  x.read_from_file(filename)
  _solver(x)