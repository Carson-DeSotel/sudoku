import math

_SIZE = 9
_MAX_SUM = 45

class Board:
  def __init__(self, size=_SIZE):
    self.size  = size
    self.board = [ [0] * self.size for i in range(self.size) ]

  def list_print(self):
    for i in range(self.size):
      print(self.board[i])

  def pretty_print(self):
    c = math.floor(self.size / 3) if (self.size / 3) > 1 else 1
    line = " " + "-" * ((7 * c) + (c - 1))

    for i in range(self.size):
      if i % 3 == 0:
        print(line)
      for j in range(self.size):
        if j % 3 == 0:
          print("| {}".format(self.board[i][j]), end = " ")
        else:
          print("{}".format(self.board[i][j]), end = " ")
      print("|")
    print(line)

  def is_complete(self):
    for i in range(self.size):
      if 0 in self.board[i]:
        return False
    return True

  # this is only valid for the standard 9x9 
  # to expand, modify constants and calculate range with
  # number of cells
  def is_valid(self):
    # validate no zeros
    if not self.is_complete():
      return False
      
    # validate each row and column
    for i in range(self.size):
      if self.sum_row(i) != 45:
        return False  
      if self.sum_col(i) != 45:
        return False
      curr_row = self.as_list_row(i)
      curr_col = self.as_list_col(i)
      curr_row.sort()
      curr_col.sort()
      if list(set(curr_row)) != curr_row:
        return False
      if list(set(curr_col)) != curr_col:
        return False
  
    # validate each cell
    for i in range(0, 3):
      for j in range(0, 3):
        ro = 3 * i
        co = 3 * j
        if self.sum_cell(ro, co) != 45:
          return False
        curr_cell = self.as_list_cell(ro, co)
        curr_cell.sort()
        if list(set(curr_cell)) != curr_cell:
          return "Err: Set Cell {} {}".format(i, j)

    return True

  def read_from_file(self, filename):
    self.board = []
    self.size = 9
    with open(filename) as fin:
      for line in fin:
        self.board.append( [
            int(num) for num in line.split()
          ] )

  def sum_row(self, index):
    s = 0
    for n in self.board[index]:
      s += n
    return s

  def sum_col(self, index):
    s = 0
    for row in self.board:
      s += row[index]
    return s

  def sum_cell(self, row_offset, col_offset):
    s = 0
    for i in range(0, 3):
      for j in range(0, 3):
        s += self.board[row_offset + i][col_offset + j]
    return s

  # so there must be some weird bug going on with references
  # I tried to just pass the row through, but that caused the 
  # array to change when I used the sort method, which invalidated
  # other bits. 
  def as_list_row(self, index):
    s = [] 
    for elem in self.board[index]:
      s.append(elem)
    return s 

  def as_list_col(self, index):
    s = []
    for r in self.board:
      s.append(r[index])
    return s 
  
  def as_list_cell(self, row_offset, col_offset):
    s = []
    for i in range(0, 3):
      for j in range(0, 3):
        s.append(self.board[row_offset + i][col_offset + j])
    return s