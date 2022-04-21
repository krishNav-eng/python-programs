from random import randint, shuffle

class SudukoPuzzleMaker:
  def __init__(self):
    self.board = []
    l = list(range(1, 10))
    shuffle(l)
    self.board.append(l)
    self.board += [[0 for _ in range(9)] for _ in range(8)]

  def make(self):
    find = self.find_empty()
    if not find:
      return True
    else:
      r, c = find
    
    tries = set()

    while len(tries) != 9:
      n = randint(1, 9)
      tries.add(n)
      if self.possible(n, r, c):
        self.board[r][c] = n

        if self.make():
          return True

        self.board[r][c] = 0
  
  def final_step(self):
    pos = set()
    # of Removed
    n = 0
    while n <= 30:
      i, j = randint(0, 8), randint(0, 8)
      if (i, j) not in pos:
        pos.add((i, j))
        pos.add((j, i))
        self.board[i][j] = 0
        self.board[j][i] = 0
        if (i, j) != (j, i):
          n+=2
        else:
          n+=1

  def possible(self, n, r, c):
    for i in range(9):
      if self.board[r][i] == n and i != c:
        return False
      if self.board[i][c] == n and i != r:
        return False

    x = (r // 3) * 3
    y = (c // 3) * 3
    for i in range(x, x+3):
      for j in range(y, y+3):
        if self.board[i][j] == n and (i, j) != (r, c):
          return False

    return True

  def find_empty(self):
    for i in range(9):
      for j in range(9):
        if self.board[i][j] == 0:
          return (i, j)

    return None
  
  

  
# Thank you :)
