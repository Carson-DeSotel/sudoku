import sys

from board import Board
from solver import solve

def main(argv):
    filename = argv[0]
    
    solve(filename)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Error: Program must have one argument...")
  else:
    main(sys.argv[1:])