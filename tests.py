from board import Board

def test_as_set_row(x):
  assert x.as_set_row(3) == {0, 2, 3, 4, 5, 8, 9}

def test_as_set_col(x):
  assert x.as_set_col(4) == {0, 5, 9}

def test_as_set_cell(x):
  assert x.as_set_cell((2, 0)) == {0, 1, 2, 3, 4, 5, 6, 8}

def test_is_valid(x):
  assert x.is_valid() == False

if __name__ == "__main__":
  x = Board(9)
  x.read_from_file("data/sud_valid_clues.txt")

  # run tests:
  test_as_set_row(x)
  test_as_set_col(x)
  test_as_set_cell(x)
  test_is_valid(x)

  print("all tests passed")