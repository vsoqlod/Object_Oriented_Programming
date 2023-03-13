import puppy_state
import state_asleep
class StatePlay(puppy_state.PuppyState):
  '''Writing the program to '''
  def play(self, puppy):
    '''As the puppy plays with you, you can continue to play with it until it becomes so exhausted that it falls asleep again (~2 or 3 times)'''
    puppy.inc_play()
    if puppy._play > 2:
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return '\nYou throw the ball again and the puppy excitedly chases it. The puppy played so much it fell asleep'
    elif puppy._play <= 2:
      return '\nYou throw the ball again and the puppy excitedly chases it.'
      
  def feed(self, puppy):
    '''When the puppy is playing, you should not be able to feed it while it is playing'''
    return '\nThe puppy is too busy playing with the ball to eat right now.'