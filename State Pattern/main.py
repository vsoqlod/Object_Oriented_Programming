"""
Jae Bum Jang
Fall 2022, 12/8
Lab 14

Create a puppy simulator program that makes use of the State pattern to create two main functions: to feed and play with the puppy. Each of these functions will have a different response depending on which state the puppy is currently in. The puppy can be in the following three states: asleep, eating, or playing.
"""
import puppy
import check_input
def main():
  '''Build a puppy object and display a menu allowing the user to choose whether to play or feed the puppy. Display the puppy's reaction to the user's choice.'''
  pup = puppy.Puppy()
  print('Congratulations on your new puppy!')
  choice = 0
  while choice != 3:
    choice = check_input.get_int_range('What would you like to do? \n1. Feed the puppy \n2. Play with the puppy \n3. Quit \nEnter choice: ', 1, 3)
    if choice == 1:
      print(pup.give_food())
    elif choice == 2:
      print(pup.throw_ball())

main()