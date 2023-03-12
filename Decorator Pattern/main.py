"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 11/30
Lab 13 - Group 17

This program creates an own personalized monster that uses three base types of monster (Alien, Beast, Undead). Users able to decorate monster with four different abilities (Fire, Flying, Laser, Poison) as many time they want, also monster update their name, hp and attack power at each time user decoration. 
"""
import alien
import beast
import undead
import fire
import flying
import lasers
import poison
import check_input 
def main():
  """Prompt users to choose which monster they want to decorate, then display the default stats of it. Next, keep prompt ability menu that users can decorate the monster, and update the monster's name and stats at each step of user decoration. Display the final monster that user created when user decide to quit."""
  print('Monster Maker!')
  choose_base_monster = check_input.get_int_range('Choose a base monster:\n1. Alien\n2. Beast\n3. Undead\nEnter choice: ', 1, 3)
  if choose_base_monster == 1:
    monster_maker = alien.Alien()
  elif choose_base_monster == 2:
    monster_maker = beast.Beast()
  elif choose_base_monster == 3:
    monster_maker = undead.Undead()
  print(monster_maker)
  choose_ability = 0
  while choose_ability != 5:
    choose_ability = check_input.get_int_range('Add an ability:\n1. Fire\n2. Flying\n3. Lasers\n4. Poison\n5. Quit\nEnter ability: ', 1, 5)
    if choose_ability == 1:
      monster_maker = fire.Fire(monster_maker)
      print(monster_maker)
    elif choose_ability == 2:
      monster_maker = flying.Flying(monster_maker)
      print(monster_maker)
    elif choose_ability == 3:
      monster_maker = lasers.Laser(monster_maker)
      print(monster_maker)  
    elif choose_ability == 4:
      monster_maker = poison.Poison(monster_maker)
      print(monster_maker)
      
  print("\nYour final monster is:")
  print(monster_maker)
  
main()
    