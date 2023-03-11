import dragon
import random
class FireDragon(dragon.Dragon):
  """Represent the Fire Dragon in the game."""
  def __init__(self, name, max_hp, f_shots):
    """Initializes the fire shots of fire dragon, call the super class(dragon) to set the max hp and the name.
    Attributes:
      name & max_hp : called from super().
      _f_shots (int) : fire shots that takes by Hero."""
    super().__init__(name, max_hp)
    self._f_shots = f_shots

  def special_attack(self, hero):
    """Special attack toward the hero, hero takes the random amount of the damage if there are fire shots left. Fire shots decrease when each time hero takes, return and display the string when hero takes it with the amount of damage value otherwise display failure of the attack."""
    if self._f_shots > 0:
      damage = random.randint(5,9)
      self._f_shots -= 1
      hero.take_damage(damage)
      return self.name+" engulfs you in flames for "+ str(damage) + " damage."
    else:
      return self.name+ " attack failed."

  def __str__(self):
    """Return and display number of remaining fire shots of fire dragon entity."""
    return super().__str__() + "\nFire shots remainings: " + str(self._f_shots)