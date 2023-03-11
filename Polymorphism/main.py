"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 10/12
Lab 8 - Group 17

This program is a game of user's trail on defeating three dragons with different skills.
"""

import fire_dragon
import flying_dragon
import hero
import dragon
import random
import check_input
def main():
  """Construct the object of Hero and create list of three dragons, let user to input Hero's name, prompt champion's quest, the start the game. Present status board of each entity with their name, hp, max hp and dragons' number of special attacks left. Prompt user which dragon to attack and display the attack menu of challenger, let user to choose which method to attack, then display attack status and return and display the message of situation. When challenger defeats one dragon, defeated dragon removes from the list, then display rest of dragons left to attack. Dragon's special attack and basic attack randomly represents, loops the trail until challenger or all dragons defeat. Prompt congratulation message if challenger defeats all dragon, otherwise prompt failure message when challenger lose."""

  name = input("What is the name, challenger? ")
  champion = hero.Hero(name, 50)
  dragons = [dragon.Dragon("Meraxes", 10), fire_dragon.FireDragon("Balerion", 15, 3), flying_dragon.FlyingDragon("Vhagar", 20, 5)]

  print(f"Welcome to dragon training, {champion.name} \nYou must defeat 3 dragons.")
  
  while champion.hp > 0 and len(dragons) > 0:
    print(f'\n{champion}')
    for i in range(len(dragons)):
      print(f"{i + 1}. Attack {dragons[i]}")
    select_dragon = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
    weapon = check_input.get_int_range("\nAttack with:\n 1. Arrow (1 D12)\n 2. Sword (2 D6)\nEnter weapon: ", 1, 2)
  
    if weapon == 1:
      print(champion.arrow_attack(dragons[select_dragon - 1]))
    elif weapon == 2:
      print(champion.sword_attack(dragons[select_dragon - 1]))
    for x in range(len(dragons)):
      if dragons[x].hp == 0:
        dragons.pop(x)
        break
    if len(dragons) > 0:
      drag = random.choice(dragons)
      drag_attack = random.randint(1, 2)
      if drag_attack == 1:
        print(drag.basic_attack(champion))
      elif drag_attack == 2:
        print(drag.special_attack(champion))
  if champion.hp > 0:
    print("\nCongratulations! You have defeated all 3 dragons, you have passed trials.")
  else:
    print("You have failed the dragon trails...")
  
main()