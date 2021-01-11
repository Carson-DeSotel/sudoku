_POSSIBLE = {1, 2, 3, 4, 5, 6, 7, 8, 9}

class Cell: 
  def __init__(self, is_clue=False, value=0, guess=_POSSIBLE):
    self.is_clue = is_clue    
    self.value   = value    # actual solution
    self.guess   = guess    # potential solutions
