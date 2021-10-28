from IllegalArgumentsException import IllegalArgumentsException

def rank_hand(hand):
  return hand.rank()
  
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
  elif len(hands) == 1:
    return hands[0]
  
  return max(hands, key = rank_hand)

  