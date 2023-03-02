# Jae Bum Jang
# Fall 2022, 8/30/22
# Program is a game of Rock, Paper, Scissors vs the computer and keeps track of score until the player decides to quit the game.

import random
import check_input


def weapon_menu():
  """User chooses between Rock, Paper, Scissors or to go back. There are no arguments. Returns R, P, S or B depending on users choice."""
  #Initialize to enter the while loop
  your_weapon = "A"
  counter = 0
  # While loop checks to make sure user input is valid
  while your_weapon != "R" and your_weapon != "P" and your_weapon != "S" and  your_weapon !="B":
    #if statement to let user know if it's invalid  
    if counter != 0:
        print("Invalid")
    print("Choose your weapon:")
    print("R. Rock")
    print("P. Paper")
    print("S. Scissors")
    print("B. Back")
    your_weapon = input()
    your_weapon = your_weapon.upper()
    counter = 1
  return your_weapon
  
 
def comp_weapon():
  """The function generates a random number from 1-3 that corresponds with a choice. There are no arguments. Returns R, 
 P or S depending on generated number"""
  comp_weapon = random.randint(1, 3)
  # If-elif statement used to change from int to string value
  if comp_weapon == 1:
    return "R"
  elif comp_weapon == 2:
    return "P"
  elif comp_weapon == 3:
    return "S"

def find_winner(player, comp):
  """The function compares the users choice vs the computers generated response. The player argument is the users choice and the comp argument is the computers choice. Returns the result of matchup and number value used to keep score."""
  #If-elif to take player argument and print statement with user's choice
  if player == "R":
    print("You chose Rock.")
  elif player == "P":
    print("You chose Paper.")
  elif player == "S":
    print("You chose Scissors.")
    
  #If-elif to take comp argument and print statement with computer's choice  
  if comp == "R":
    print("Computer chose Rock.")
  elif comp == "P":
    print("Computer chose Paper.")
  elif comp == "S":
    print("Computer chose Scissors.")

  #If-elif to determine the winner or if game ended in a tie, returns the result
  if player == "R" and comp == "S":
    print("You win")
    return 1
  elif player == "R" and comp == "P":
    print("Computer wins")
    return 2
  elif player == "S" and comp == "R":
    print("Computer wins")
    return 2
  elif player == "S" and comp == "P":
    print("You win")
    return 1
  elif player == "P" and comp == "R":
    print("You win")
    return 1
  elif player == "P" and comp == "S":
    print("Computer wins")
    return 2
  elif player == comp:
    print("Tie")
    return 0

def display_scores(player, comp):
  """This function displays the current score of game. The player parameter is user's score and the comp parameter is the computer's score. Returns print statement that displays score."""
  print(f"Player =", player)
  print(f"Computer =", comp)


def main():
  """"""
  menu_input = 0
  user_score = 0
  comp_score = 0
  user_weapon = ""
  # While loop to keep user interacting until 3 is pressed to quit
  while menu_input != 3:
    print("RPS Menu:")
    print("1. Play game")
    print("2. Show Score")
    print("3. Quit")
  
    menu_input = check_input.get_int_range("", 1, 3)
    # if statement keeps user in game until "B" (back) is input
    if menu_input == 1:
      user_weapon = weapon_menu()
      computer_weapon = comp_weapon()
      # while loop checks to see if user presses "B" for back           to main menu
      while user_weapon != "B":
        winner = find_winner(user_weapon, computer_weapon)
        # if-elif to keep count of score
        if winner == 1:
          user_score += 1
        elif winner == 2:
          comp_score += 1
        user_weapon = weapon_menu()
        computer_weapon = comp_weapon()
    #elif calls function to display score
    elif menu_input == 2:
      display_scores(user_score, comp_score)
      
  print("Final Score: ")
  display_scores(user_score, comp_score)



main()
