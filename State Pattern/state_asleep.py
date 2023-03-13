import puppy_state
import state_eat
class StateAsleep(puppy_state.PuppyState):
  '''The purpose of this class is to explain how puppies react when we play with them or feed them while they are playing.'''
  
  def play(self, puppy):
    '''The puppy doesnt want to play when they are sleeping'''
    return "\nThe puppy is asleep. It doesn't want to play right now."
    
  def feed(self, puppy):
    '''There is only one way to wake a puppy up when it is asleep, and that is by feeding it. Once the puppy hears its food bowl being filled, it will come running.''' 
    puppy.change_state(state_eat.StateEat())
    puppy.inc_feed()
    return '\nThe puppy wakes up and comes running to eat.'
