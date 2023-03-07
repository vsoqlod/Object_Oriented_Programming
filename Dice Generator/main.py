"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 9/27
Lab 6 - Group 16

This program is a dice game using 3 dices that user can obtain points for pair, all three of kind and series. User can select wheter continue or exit, and final score display at the end.
"""

import die
import player
import check_input

def take_turn(turn):
  """Roll the player's dices, display each dices, check for and prompt each win types, and display updated score at every turn.
  Args:
    turn: Player object passes from main()"""
  turn.roll_dice()
  print(turn)
  if turn.has_three_of_a_kind():
    print("You got 3 of a kind!")
  elif turn.has_pair():
    print("You got a pair!")
  elif turn.has_series():
    print("You got a series of 3.")
  else:
    print("Aww.\tToo Bad.")
  print(f"score = {turn.get_points()}")

def main():
  """Implement the game and prompt user to continue or exit, check if user input is invalid and prompt user again for proper input. Display the prompt when game is over with final score."""
  print("-Yahtzee-\n")
  dice123 = player.Player()
  take_turn(dice123)
  while check_input.get_yes_no("Play again? (Y/N): "):
    print()
    take_turn(dice123)
  print("\nGame Over")
  print(f"Final Score = {dice123.get_points()}")
  
  
main()