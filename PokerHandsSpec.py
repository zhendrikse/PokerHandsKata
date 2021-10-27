from Hand import Hand
from PokerHands import poker
from mamba import description, context, it 
from expects import expect, equal, raise_error
from IllegalArgumentsException import IllegalArgumentsException
from mockito import when

import PokerHands

straight_flush = Hand("6C 7C 8C 9C T9".split())
four_of_a_kind = Hand("D9 H9 S9 C9 D7".split())
full_house = Hand("TD TC TH 7C 7D".split())

when(PokerHands).hand_rank(full_house).thenReturn(1)
when(PokerHands).hand_rank(four_of_a_kind).thenReturn(2)
when(PokerHands).hand_rank(straight_flush).thenReturn(3)

with description('Given an empty set of hands') as self:
  with context('When trying to rank the hands'):
    with it('should raise an exception'):
      expect(lambda: poker([])).to(raise_error(IllegalArgumentsException))

with description('Given a set of one hand') as self:
  with context('When trying to rank the hands'):
    with it('should return the one and only hand'):
      hands = [straight_flush]
      expect(poker(hands)).to(equal(straight_flush))

with description('Given four of a kind versus full house') as self:
  with context('When trying to rank the hands'):
    with it('should return the four of a kind hand'):
      hands = [four_of_a_kind, full_house]
      expect(poker(hands)).to(equal(four_of_a_kind))

with description('Given full house versus full house') as self:
  with context('When trying to rank the hands'):
    with it('should return the full house hand'):
      hands = [full_house, full_house]
      expect(poker(hands)).to(equal(full_house))

with description('Given 99 straight flushes versus full house') as self:
  with context('When trying to rank the hands'):
    with it('should return the straight flush hand'):
      hands = [full_house] + 99 * [straight_flush]
      expect(poker(hands)).to(equal(straight_flush))

with description('Given a set of straight flush, four of a kind and full house') as self:
  with context('When trying to rank the hands'):
    with it('should return the straight flush hand'):
      hands = [straight_flush, four_of_a_kind, full_house]
      expect(poker(hands)).to(equal(straight_flush))


