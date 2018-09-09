def make_bricks(small, big, goal):
  if big is not 0 and goal % 5 <= small:
      return True
  return False