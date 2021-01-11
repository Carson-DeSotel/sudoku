from board import Board 
from board import _SIZE
import math 

def _solver(x):
  while not x.is_valid():
    for i in range(_SIZE):
      for j in range(_SIZE):
        if len(x.board[i][j].guess) == 1:
          t = x.board[i][j].guess.pop()
          x.board[i][j].value = t
          x.regenerate_possibilities(t, i, j)

def solve(filename):
  x = Board()
  x.read_from_file(filename)
  print("CLUES:")
  x.pretty_print()
  _solver(x)
  print("SOLVED")
  x.pretty_print()
  print("VALID:", x.is_valid())