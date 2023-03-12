import abc
import monster
class Decorator(monster.Monster, abc.ABC):
  """Represent decorator for each monster on their ability
  Attributes:
    _monster: construct monster as monst
    __init__: construct the monster's name and hp"""
  def __init__(self, monst):
    """Initialize monster as monst and it's name and hp using super function"""
    self._monster = monst
    super().__init__(monst.name, monst.hp)
    
  def attack(self):
    """Return attack on the monster attribute"""
    return self._monster.attack()
    