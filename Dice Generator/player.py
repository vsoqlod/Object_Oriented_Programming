import die

class Player:
  """Represents a list of three Die objects and player's point.
    Attributes:
      die (list): list of of 3 Die objects
      points (int): the player's point"""

  def __init__(self):
    """Set and sort a list of three die objects, initialize player's points to zero"""
    self.dice = [die.Die(), die.Die(), die.Die()]
    self.dice.sort()
    self.points = 0

  def get_points(self):
    """Return the player's point"""
    return self.points

  def roll_dice(self):
    """Roll each die objects in the dice list using for loop and then sorts the list"""
    for d in self.dice:
      d.roll()
    self.dice.sort()

  def has_pair(self):
    """Return true if two dice has same value and increment the point by 1, returns false for rest """
    if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2]:
      self.points += 1
      return True
    return False

  def has_three_of_a_kind(self):
    """Return true if all three dice have same value and increment the points by 3, returns false for rest"""
    if self.dice[0] == self.dice[1] == self.dice[2]:
      self.points += 3
      return True
    return False
    
  def has_series(self):
    """Return truen if value of dice has in order of series and increment the points by 2, returns false for rest"""
    if self.dice[1] - self.dice[0] == 1 and self.dice[2] - self.dice[1] == 1:
      self.points += 2
      return True
    return False

  def __str__(self):
    """Return string with in the format of "D1 = value, D2 = value, D3= value" """
    string = ""
    self.dice.sort()
    for i, d in enumerate(self.dice):
      string += "D" + str(i + 1) + "= " + str(d) + " "
    return string