class Entity:
  """Represent an Entity which is a characters in the game.
  Attributes:
    name (str): name of characters in the game.
    hp (int) : hp of characters in the game.
    max_hp (int): max hp of characters in the game."""
  
  def __init__(self, name, max_hp):
    """Initialize the name, and set the hp, max hp to max hp."""
    self._max_hp = max_hp
    self._hp = max_hp
    self._name = name
    
  def take_damage(self, dmg):
    """Damage sustain by characters. Subtract the damage value from the entity’s hp, set the lowest hp to be zero, negative value also become zero."""
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """Returns and display entity's name and hp / max hp."""
    return self._name + ": " + str(self._hp) + "/" + str(self._max_hp)
    
  @property
  def name(self):
    """Returns the name of entity."""
    return self._name
    
  @property
  def hp(self):
    """Returns the hp of entity."""
    return self._hp
