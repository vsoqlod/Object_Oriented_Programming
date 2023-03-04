"""
Jae Bum Jang
Fall 2022, 9/14/22
State capitals quiz program that quizes user on the state capitals based on the text file.
Prompts 10 questions, each question presents 4 options that users can answer.
"""

import random

def read_file_to_dict(file_name):
  """Convert the infromation(state, capitals) in text file to dictionary.
  Args: 
    file_name: StateCapitals.txt
  Returns: 
    dictionary: dictionary that converted from the text file """
  dictionary = {}
  file = open(file_name)
  my_list = []
  for line in file:
    text = line.strip().split(',')
    for i in range(2):
      my_list.append(text[i])
  for index in range(0, len(my_list), 2):
    dictionary[my_list[index]] = my_list[index+1]
  return dictionary

  
def get_random_state(states):
  """Randomly choose key as a value from the list of dictionary's keys.
  Args:
    states(str): "f" state that passed from main()
  Returns: 
    random_state: state, capital pair randomly chosen from the list"""
  states_list = list(states.keys())
  random_state = states_list[random.randint(0, len(states_list)-1)]
  return random_state


def get_random_choices(states, correct_capital):
  """Create a list which contain 4 value, 1 answer for the state and 3 incorrect random capitals from list of dictionary's value.
  Args:
    states(str): "f" state that passed from main() 
    correct_capital: "f[e]" correct capital among the 4 passed from main()
  Returns:
    random.sample(capital_answe_list,4) : list using random()"""
  capital_list = list(states.values())
  capital_answer_list = [correct_capital]
  while len(capital_answer_list) < 4:
    incorrect_answer = capital_list[random.randint(0,len(capital_list)-1)]
    if incorrect_answer not in capital_answer_list:
      capital_answer_list.append(incorrect_answer)
  return random.sample(capital_answer_list, 4)
  

def ask_question(correct_state, possible_answers):
  """Prompt question to users and ask for their choices of the capital according to that state.
  Args: 
    correct_state: "e", the correct state passed from main()
    possible_answers: "d", list of random 4 possible answer passed from main()
    """
  print('The capital of', correct_state, 'is:')
  print('\tA. %s \tB. %s \tC. %s \tD. %s' % (possible_answers[0], possible_answers[1], possible_answers[2], possible_answers[3]))
  selection = input('Enter selection: ').upper()
  while selection not in ['A','B','C','D']:
    print('Invalid input. Input choice A-D')
    selection = input('Enter selection:').upper()
  if selection == 'A' :
    return 0
  elif selection == 'B' :
    return 1
  elif selection == 'C' :
    return 2
  elif selection =='D' :
    return 3

def main():
  """Read the text file, then repeats 10 times using for loop and count. If user' inputs other then A-D, let them know its incorrect and give them another trial. After all following 10 questions, display end of test and how many answers users got."""
  count = 0
  print('- State Capitals Quiz -')
  for time in range(1, 11):
    f = read_file_to_dict('StateCapitals.txt')
    e = get_random_state(f)
    d = get_random_choices(f, f[e])
  
    print(time, end=". ")
    if d[ask_question(e, d)] == f[e]:
      print('Correct!')
      count += 1
    else:
      print('Incorrect! The correct answer is:', f[e])
  print('End of test. You got %s correct.' % count)
main()