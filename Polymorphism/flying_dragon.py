import dragon
import random

class FlyingDragon(dragon.Dragon):
  """Initializes the swoops of flying dragon, call the super class(dragon) to set the max hp and the name.
    Attributes:
      name & max_hp : called from super().
      _swoops (int) : swoops that takes by Hero."""
  def __init__(self, name, max_hp, swoops):
    super().__init__(name, max_hp)
    self._swoops = swoops

  def special_attack(self, hero):
    """Special attack toward the hero, hero takes the random amount of the damage if there are swoops left. Swoops decrease when each time hero takes, return and display the string when hero takes it with the amount of damage value otherwise display failure of the attack."""
    if self._swoops > 0:
      damage = random.randint(5,9)
      self._swoops -= 1
      hero.take_damage(damage)
      return self.name+" swoops and slashes you for "+str(damage) + " damage."
    else:
      return self.name+ " attack failed."

  def __str__(self):
    """Return and display number of remaining swoop attacks of flying dragon entity."""
    return super().__str__() + "\nSwoops attacks remainings: " + str(self._swoops)