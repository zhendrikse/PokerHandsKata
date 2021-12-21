from hand import Hand
from poker_hands import determine_best_hand
from mamba import description, context, it, fdescription 
from expects import expect, equal, raise_error
from IllegalArgumentsException import IllegalArgumentsException
from mockito import when
from poker_ranks import PokerRanks

import poker_hands

straight_flush = Hand("6C 7C 8C 9C T9")
four_of_a_kind = Hand("D9 H9 S9 C9 D7")
full_house = Hand("TD TC TH 7C 7D")
two_pairs = Hand("5S 5D 9H 9C 6S")
ace_5_staight = Hand("AS 2S 3S 4S 5S")
ace_6_staight = Hand("2C 3C 4C 5S 6S")
ace_heigh = Hand("AS 2S 3S 4S 6C")
seven_heigh = Hand("2S 3S 4S 6C 7D")

when(poker_hands).rank_hand(full_house).thenReturn(PokerRanks.FULL_HOUSE.value)
when(poker_hands).rank_hand(straight_flush).thenReturn(PokerRanks.STRAIGHT_FLUSH.value)

with description("Ranking hands") as self:

  with description('Given an empty set of hands'):
    with it('raises an exception'):
      expect(lambda: determine_best_hand([])) \
        .to(raise_error(IllegalArgumentsException))

  with description('Given a set of one hand'):
    with it('returns the one and only hand as winner'):
      hands = [straight_flush]
      expect(determine_best_hand(hands)).to(equal(straight_flush))

  with description('Given full house versus straight flush') as self:
    with it('returns the straight flush hand'):
      hands = [full_house, straight_flush]
      expect(determine_best_hand(hands)).to(equal(straight_flush))

  with description('Given straight flush versus full house') as self:
    with it('returns the straight flush hand'):
      hands = [straight_flush, full_house]
      expect(determine_best_hand(hands)).to(equal(straight_flush))


  # with description('and the other has four of a kind'):
  #     with it('returns the four of a kind hand as winner'):
  #       hands = [full_house, four_of_a_kind]
  #       expect(determine_best_hand(hands)).to(equal(four_of_a_kind))
  # with context("Given one hand has a full house"):
  #   with description('and the other has also full house'):
  #       with it('returns the four of a kind hand as winner'):
  #         hands = [full_house, full_house]
  #         expect(determine_best_hand(hands)).to(equal(full_house))
  #   with context('and 99 straight flushes'):
  #     with it('returns the straight flush hand as winner'):
  #       hands = [full_house] + 99 * [straight_flush]
  #       expect(determine_best_hand(hands)).to(equal(straight_flush))
  #   with context('and a set of straight flush as well as four of a kind'):
  #     with it('returns the straight flush hand as winner'):
  #       hands = [straight_flush, four_of_a_kind, full_house]
  #       expect(determine_best_hand(hands)).to(equal(straight_flush))


