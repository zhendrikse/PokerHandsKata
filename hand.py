from poker_ranks import PokerRanks

class Hand:
  def __init__(self, cards: str) -> None:
    self.cards = cards.split()

  def straight(self):
    pass

  def flush(self):
    pass

  def kind(self, kind_of: int):
    pass

  def rank(self) -> PokerRanks:
    if self.straight() and self.flush():
      return PokerRanks.STRAIGHT_FLUSH
    elif self.kind(4):
      return PokerRanks.FOUR_OF_A_KIND
    elif self.straight():
      return PokerRanks.STRAIGHT
    return PokerRanks.FLUSH