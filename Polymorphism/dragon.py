import entity
import random
class Dragon(entity.Entity):
  """Represent dragons in the game."""

  def basic_attack(self, hero):
    """Basic attack of dragons, damage randomly range from 3 to 7. Returns and display tail attack and damage value toward the Hero."""
    damage = random.randint(3,7)
    hero.take_damage(damage)
    return self.name+" smashes you with its tail for "+str(damage) + " damage."

  def special_attack(self, hero):
    """Special attack of dragons, damage randomly range from 4 to 8. Returns and display claw attack and damage value toward the Hero."""
    damage = random.randint(4,8)
    hero.take_damage(damage)
    return self.name+" scratches you with its claws for "+str(damage) + " damage."
  