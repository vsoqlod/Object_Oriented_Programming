"""
Jae Bum Jang
Fall 2022, 9/21
Group 17

This program present user to make a rectangle within dimension of width and height 1 to 5. Then able to move the rectangle inside 20*20 grid.  
"""

import rectangle
import check_input


def display_grid(grid):
  """Display the elements of the grid Args: grid: list passed from main() that will be displayed"""
  for row in grid:
    for element in row:
      print("%2s" % element, end="")
    print()


def reset_grid(grid):
  """Reset the elements of the grid with '.'
  Args: 
    grid: list passed from main() that will be reseted"""
  for row_index in range(20):
    for column_index in range(20):
      grid[row_index][column_index] = '.'


def place_rect(grid, rect):
  """Place the rectangle on the designated coordinate
  Args:
      grid: list passed from main() that will be updated
      rect: rectangle that will be place on the grid"""
  for row_index in range(rect.get_height()):
   for column_index in range(rect.get_width()):
      grid[row_index - rect.y][column_index - rect.x] = '*'


def main():
  """Prompt user to input size of the rectangle height and width between 1 to 5, then represent grid size of 20*20 using 2D list, prompt user to choose direction of the rectangle inside the grid. Warn user if they inputted invalid inputs and let them input again."""
  menu_input = 0
  grid = []
  for row_index in range(20):
    table_row = ['.'] * 20
    grid.append(table_row)
  rectangle_height = check_input.get_int_range('Enter the rectangle heigth (1-5): ', 1, 5)
  rectangle_width = check_input.get_int_range('Enter the rectangle width (1-5):  ', 1, 5)
  rect = rectangle.Retangle(rectangle_width, rectangle_height)
  print()
  while menu_input != 5:
    reset_grid(grid)
    place_rect(grid, rect)
    display_grid(grid)
    menu_input = check_input.get_int_range("\nEnter Direction: \n1. Up\n2. Down\n3. Left\n4. Right\n5. Quit\n",1, 5)
    print()
    if menu_input == 1:
      if rect.y < 0:
        rect.move_up()
      else:
        print('Error! The rectangle moves past the boundaries. Please choose the other options.')
        print()
    elif menu_input == 2:
      if 20 - rect.get_height() + rect.y > 0:
        rect.move_down()   
      else:
        print('Error! The rectangle moves past the boundaries. Please choose the other options.')
        print()
    elif menu_input == 3:
      if rect.x < 0:
        rect.move_left()
      else:
        print('Error! The rectangle moves past the boundaries. Please choose the other options.')
        print()
    elif menu_input == 4:
      if 20 - rect.get_width() + rect.x > 0: 
        rect.move_right() 
      else:
        print('Error! The rectangle moves past the boundaries. Please choose the other options.')
        print()
    else:
      break
main()