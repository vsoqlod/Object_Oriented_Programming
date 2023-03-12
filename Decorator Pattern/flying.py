import decorator
class Flying(decorator.Decorator):
  """Represent Flying ability of the dragon
Attribute:
  monst: each monster"""
  def __init__(self, monst):
    """Update monster's name, hp pertains to the skill, return it to monster itself using super function"""
    monst.name = 'Flying ' + monst.name
    monst.hp = monst.hp + 4
    self._monster = monst
    super().__init__(self._monster)
    
  def attack(self):
    """call attack using super function and add the power of attack pertains to this ability"""
    return super().attack() + 1