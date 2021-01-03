import sys
import math
from board import Board

def main(argv):
    filename = argv[0]
    x = Board(0)
    x.read_from_file(filename)
    print(x.is_valid())

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Error: Program must have one argument...")
  else:
    main(sys.argv[1:])