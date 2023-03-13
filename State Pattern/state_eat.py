import puppy_state
import state_play
import state_asleep

class StateEat(puppy_state.PuppyState):
  '''We will write the program how the puppy reacts when we play with him or feed him while he is eating in this class.'''
  def play(self, puppy):
    '''Suppose it is eating -- the puppy has to eat until it is so full that it will fall asleep (after 2 or 3 times)'''
    puppy.change_state(state_play.StatePlay())
    puppy.inc_play()
    return '\nThe puppy looks up from its food and chases the ball you threw.'
    
  def feed(self, puppy):
    '''If you can distract it with a ball, then it may play with you if you distract it with it.'''
    puppy.inc_feed()
    if puppy._feed > 2:
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return '\nThe puppy continues to eat as you add another scoop of kibble to its bowl. The puppy ate so much it fell asleep!'
    elif puppy._feed <= 2:
      return '\nThe puppy continues to eat as you add another scoop of kibble to its bowl.'