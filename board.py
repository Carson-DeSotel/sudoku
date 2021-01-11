import math
from cell import Cell 
from cell import _POSSIBLE 

_SIZE = 9

class Board:
  def __init__(self, size=_SIZE):
    self.size   = size
    self.board  = [
      [ Cell() for x in range(self.size) ]
      for y in range(self.size)
    ]

  def pretty_print(self):
    c = math.floor(self.size / 3) if (self.size / 3) > 1 else 1
    line = " " + "-" * ((7 * c) + (c - 1))

    for i in range(self.size):
      if i % 3 == 0:
        print(line)
      for j in range(self.size):
        if j % 3 == 0:
          print("| {}".format(self.board[i][j].value), end = " ")
        else:
          print("{}".format(self.board[i][j].value), end = " ")
      print("|")
    print(line)

  def read_from_file(self, filename):
    fin = open(filename)
    self.size = int(fin.readline())
    t = []
    for line in fin:
      for n in line.split():
        t.append(int(n))          
    fin.close()

    for i in range(self.size):
      for j in range(self.size):
        to_add = t.pop(0)
        self.board[i][j].value = to_add
        if to_add != 0:
          self.board[i][j].is_clue = True

  def as_set_row(self, index):
    s = set()
    for elem in self.board[index]:
      s.add(elem.value)
    return s 

  def as_set_col(self, index):
    s = set()
    for r in self.board:
      s.add(r[index].value)
    return s 
  
  def as_set_cell(self, row_offset, col_offset):
    s = set()
    for i in range(0, 3):
      for j in range(0, 3):
        s.add(self.board[row_offset + i][col_offset + j].value)
    return s

  def print_possibilities(self):
    for i in range(self.size):
      for j in range(self.size):
        print(i, j, self.board[i][j].guess)

  def generate_possibilities(self):
    for i in range(self.size):
      for j in range(self.size):
        if self.board[i][j].is_clue:
          self.board[i][j].guess = set()
        else:
          t = self.board[i][j].guess - self.as_set_row(i) 
          self.board[i][j].guess = t
          t = self.board[i][j].guess - self.as_set_col(j)
          self.board[i][j].guess = t  
          ro = math.floor(i / 3)
          co = math.floor(j / 3)
          t = self.board[i][j].guess - self.as_set_cell(ro, co)
          self.board[i][j].guess = t

  # NOTE: discard is used to avoid raising KeyErrors in case where
  #       element is not in the list
  def regenerate_possibilities(self, e, i, j):
    for x in range(self.size):
      self.board[i][x].guess.discard(e)
      self.board[x][j].guess.discard(e)
    
    ro = 3 * i 
    co = 3 * j
    for x in range(0, 3):
      for y in range(0, 3):
        self.board[ro + x][co + y].guess.discard(e)

  def is_complete(self):
    for i in range(self.size):
      for j in range(self.size):
        if self.board[i][j].value == 0:
          return False
    return True

  def is_valid(self):
    # validate no zeros
    if not self.is_complete():
      return False
      
    for x in range(self.size):
      if (self.as_set_row(x) != _POSSIBLE 
      or self.as_set_col(x) != _POSSIBLE):
        return False

    for i in range(0, 3):
      for j in range(0, 3):
        ro = 3 * i 
        co = 3 * j 
        if self.as_set_cell(ro, co) != _POSSIBLE:
          return False
  
    return True