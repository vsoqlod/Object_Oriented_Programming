import state_asleep
class Puppy:
  '''Interaction between the user and the object.
     Input attributes: state, feeds, _plays - add properties for feeds and plays.'''
  @property
  def feed(self):
    """The function helps to get feed"""
    return self._feed
    
  @property
  def play(self):
    """The function helps to get play"""
    return self._play
  
  def __init__(self):
    '''The state is initialized to asleep, and the number of feeds and plays is then initialized.'''
    self._state = state_asleep.StateAsleep()
    self._feed = 0
    self._play = 0
  
  
  def change_state(self, new_state):
    '''This update changes the puppy's state to the new one'''
    self._state = new_state
    
  def throw_ball(self):
    '''Calls the play method for whichever state the puppy is in'''
    return self._state.play(self)
  
  def give_food(self):
    '''Calls the feed method based on the state of the puppy at any given time'''
    return self._state.feed(self)

  def inc_feed(self):
    '''A number is incremented every time the puppy has been fed in a row'''
    self._feed += 1

  def inc_play(self):
    '''The number of times that the puppy has been played with in a row will be incremented.'''
    self._play += 1

  def reset(self):
    '''The feeds and plays attributes are reinitialized.'''
    self._feed = 0
    self._play = 0