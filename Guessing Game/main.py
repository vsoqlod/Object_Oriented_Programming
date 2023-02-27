# Jae Bum Jang
# 8/23/2022
# This program randomly generates number from 1 to 100 and prompts user to guess that random number.

import random
import check_input


def main():
  # assign a random variable
  val = random.randint(1,100)
  print("- Guessing Game –")
  print("I’m thinking of a number. ", end = " ")
  num = check_input.get_int_range(" Make a guess (1-100):", 1, 100)
  # we start tries from 1 and we keep on going from there, and that includes the first try.
  count = 1
  # while the guess is wrong then promt the user to keep on trying
  while num != val:
    #To account for the try Count+1
    count += 1
      #if guess is less than val then Too low = Output
    if num < val:
      print("Too Low.", end = " ")
      num = check_input.get_int_range("Guess again (1-100): ", 1, 100)
      #if guess is higher than val then Too high = Output
    elif num > val:
      print("Too high.", end = " ")
      num = check_input.get_int_range("Guess again (1-100): ", 1, 100)      
    #Output the number of tries and congratulate the user. 
  print("Correct!  You got it in "+ str(count) + " tries.")
main()
