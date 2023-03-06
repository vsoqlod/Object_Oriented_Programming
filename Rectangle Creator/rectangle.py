class Retangle:
  
  def __init__(self, w, h): 
    """contructor that initializes width, height as w and h, x and y as (0,0)"""
    self.width = w
    self.height = h
    self.x = 0
    self.y = 0
    
  def get_coords(self):
    """returns the x and y value as a pair"""
    return (self.x, self.y)
    
  def get_width(self):
    """returns width of rectangle"""
    return self.width
    
  def get_height(self):
    """returns height of rectangle"""
    return self.height
    
  def move_up(self):
    """moves the rectangle 1 up of the y coordinate"""
    self.y += 1
    
  def move_down(self):
    """moves the rectangle 1 down of the y coordinate"""
    self.y -= 1
    
  def move_left(self):
    """moves the rectangle 1 up of the x coordinate"""
    self.x += 1

  def move_right(self):
    """moves the rectangle 1 down of the x coordinate"""
    self.x -= 1
