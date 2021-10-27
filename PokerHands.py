from IllegalArgumentsException import IllegalArgumentsException

def hand_rank(hand):
  return hand.rank()
  
# Return the best hand: poker([hand,...]) => hand 
def poker(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
  elif len(hands) == 1:
    return hands[0]
  
  return max(hands, key = hand_rank)

  