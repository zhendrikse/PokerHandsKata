from mamba import description, context, it, before, fcontext
from expects import expect, equal, have_len, raise_error, be_true, be_false
from hand import Hand
from poker_ranks import PokerRanks

with description(Hand):
  with context('with ace low straight'):
    with it('ranks the hand accordingly'):
      ace_low_straight = Hand("AC 2D 4H 3D 5S")
      expect(ace_low_straight.rank_hand()).to(equal(
       (PokerRanks.STRAIGHT, 5)
      ))








      