import monster
class Alien(monster.Monster):
  """Represent Alien which is one of 3 monsters"""
  def __init__(self):
    """Initializes the name of the monster and default hp using super function."""
    super().__init__('Alien', 5)

  def attack(self):
    """Return amount of damage of the attack that monster will cause"""
    return 5