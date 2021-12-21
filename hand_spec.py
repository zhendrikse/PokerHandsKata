from mamba import description, context, it, before
from expects import expect, equal, raise_error
from hand import Hand
from poker_ranks import PokerRanks
from mockito import when

#full_house = Hand("TD TC TH 7C 7D")
straight_flush = Hand("6C 7C 8C 9C T9")
ace_5_staight = Hand("AS 2S 3S 4S 5S")
flush = Hand("2D 4D 6D 9D 10D")
four_of_a_kind = Hand("D9 H9 S9 C9 D7")

with description(Hand):
  with context("Given a hand with straight"):
    with before.each:
      when(Hand).straight().thenReturn(True)

    with it('ranks the hand as straight'):
      expect(ace_5_staight.rank()).to(equal(PokerRanks.STRAIGHT))
    with description('and flush') as self:
        with it('ranks the hand as straight flush'):
          when(Hand).flush().thenReturn(True)
          expect(straight_flush.rank()).to(equal(PokerRanks.STRAIGHT_FLUSH))

  with context('Given a hand with flush') as self:
      with it('ranks the hand as flush'):
        when(Hand).straight().thenReturn(False)
        expect(flush.rank()).to(equal(PokerRanks.FLUSH))

  with context('Given a hand with four of a kind') as self:
      with it('ranks the hand as four of a kind'):
        when(Hand).kind(4).thenReturn(True)
        expect(four_of_a_kind.rank()).to(equal(PokerRanks.FOUR_OF_A_KIND))


      