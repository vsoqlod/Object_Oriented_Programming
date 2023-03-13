import abc
class PuppyState(abc.ABC):
  """Abstract class - Allow user to feed or play with the pet
  Attribute:
    <abstract> play(self, puppy)
    <abstract> attack(self, puppy)"""
  @abc.abstractmethod
  def play(self, puppy):
    '''all puppy state subclasses must override an abstract method (no code)'''
    pass
  
  @abc.abstractmethod
  def feed(self, puppy):
    '''all puppy state subclasses must override an abstract method (no code)'''
    pass