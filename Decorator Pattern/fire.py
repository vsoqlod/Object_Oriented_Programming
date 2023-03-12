import decorator
class Fire(decorator.Decorator):
  """Represent fire ability of the dragon
  Attribute:
    monst: each monster"""
  def __init__(self, monst):
    """Update monster's name, hp pertains to the skill, return it to monster itself using super function"""
    monst.name = 'Fiery ' + monst.name
    monst.hp = monst.hp + 4
    self._monster = monst
    return super().__init__(self._monster)

  def attack(self):
    """call attack using super function and add the power of attack pertains to this ability"""
    return super().attack() + 3

