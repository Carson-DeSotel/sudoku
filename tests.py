from board import Board

def test_as_set_row(x):
  assert x.as_set_row(3) == {0, 2, 3, 4, 5, 8, 9}

def test_as_set_col(x):
  assert x.as_set_col(4) == {0, 5, 9}

def test_as_set_cell(x):
  assert x.as_set_cell((2, 0)) == {0, 1, 2, 3, 4, 5, 6, 8}

def test_is_valid(x):
  assert x.is_valid() == False

def test_generate_possibilities(x):
  x.generate_possibilities()
  assert x.board[0][0].guess == {2, 3, 9}, "(0,0): {}".format(x.board[0][0].guess)
  assert x.board[0][1].guess == {2, 6, 9}, "(0,1): {}".format(x.board[0][1].guess)
  assert x.board[0][2].guess == set(),     "(0,2): {}".format(x.board[0][2].guess)
  assert x.board[1][0].guess == {2, 8},    "(1,0): {}".format(x.board[1][0].guess)
  assert x.board[1][1].guess == {2, 4},    "(1,1): {}".format(x.board[1][1].guess)
  assert x.board[1][2].guess == set(),     "(1,2): {}".format(x.board[1][2].guess)
  assert x.board[2][0].guess == {3, 9},    "(2,0): {}".format(x.board[2][0].guess)
  assert x.board[2][1].guess == {4, 9},    "(2,1): {}".format(x.board[2][1].guess)
  assert x.board[2][2].guess == {1},       "(2,2): {}".format(x.board[2][2].guess)

def test_regenerate_possibilities(x):
  x.generate_possibilities()
  x.board[2][2].value = 1
  x.regenerate_possibilities(1, 2, 2)

  assert x.board[2][2].guess == set(),     "(2,2): {}".format(x.board[2][2].guess)
  assert x.board[2][4].guess == {3,4},     "(2,4): {}".format(x.board[2][4].guess)
  assert x.board[2][7].guess == {7},       "(2,7): {}".format(x.board[2][7].guess)
  assert x.board[4][2].guess == {8},       "(4,2): {}".format(x.board[4][2].guess)

def test_is_valid_complete(x):
  assert x.is_valid() == True

if __name__ == "__main__":
  x = Board(9)
  x.read_from_file("data/sud_valid_clues.txt")

  # run tests:
  test_as_set_row(x)
  test_as_set_col(x)
  test_as_set_cell(x)
  test_is_valid(x)
  test_generate_possibilities(x)
  test_regenerate_possibilities(x)

  x.read_from_file("data/sud_valid.txt")
  test_is_valid_complete(x)

  print("all tests passed")