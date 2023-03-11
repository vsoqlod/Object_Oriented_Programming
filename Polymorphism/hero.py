import entity
import random
class Hero(entity.Entity):
  """Represents the Hero of the game."""

  def sword_attack(self, dragon):
    """Sword attack of Hero, damage randomly range from 2 to 12 (2 dice with each damage value = 1~6 + 1~6). Return and display attack and damage value toward the dragon."""
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    damage = d1 + d2
    dragon.take_damage(damage)
    return "\nYou slash the "+ dragon.name + " with your sword for "+str(damage) + " damage."
    

  def arrow_attack(self, dragon):
    """Arrow attack of Hero, damage randomly range from 1 to 12 (1 dice with damage range = 1~12). Return and display attack and damage value toward the dragon."""
    damage = random.randint(1,12)
    dragon.take_damage(damage)
    return "\nYou hit "+ dragon.name + " with an arrow for "+ str(damage) + " damage."