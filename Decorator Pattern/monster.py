import abc
class Monster(abc.ABC):
  """Represent abstract of the monster
  Attributes:
    name(str) : name of the monster
    hp(int) : hp of the monster"""
  def __init__(self, name, hp):
    """Initialize the name and the hp of the monsters"""
    self._name = name
    self._hp = hp

  def __str__(self):
    """Return a string og the name, hp, and attack type of the monster."""
    return '\nName: ' + self._name + '\nHP: ' + str(self._hp) + '\nAttack: ' + str(self.attack())

  @abc.abstractmethod
  def attack(self):
    """Represent abstract of the attack"""
    pass
  
  @property
  def name(self):
    """return the name"""
    return self._name

  @name.setter
  def name(self, name):
    """setter for the name"""
    self._name = name
    
  @property
  def hp(self):
    """return the hp"""
    return self._hp

  @hp.setter
  def hp(self, hp):
    """setter for the hp"""
    self._hp = hp