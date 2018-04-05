# I don't feel great about this.
# 

def camel_to_sentence(camel):
  # no regex
  # thought about doing ascii comparison but i think this is quicker...
  uppers = ['A', 'B', 'C', ..., 'Z']

  # get indexes of all uppercase letters
  split = []
  for idx, letter in enumerate(camel):
    if letter in uppers:
      split.append(idx)

  # split on previously collected indexes
  # these two steps could have been done in one iteration.
  # moving on because of time.i
  previous = 0
  sentence = []
  for idx, upper_idx in enumerate(split):

    if idx == 0:
      # i do not remember if `substring` is inclusive at the beginning or end....
      # moving on since time is valuable
      sentence.append(camel.substring(0, upper_idx - 1)).lower()

    sentence.append(camel.substring(previous, upper_idx - 1)).lower()
    previous = upper_idx

  # capitalize the first word of the sentence
  sentence[0][0].upper()

  return ' '.join(sentence)