from mamba import description, context, it 
from expects import expect, equal, raise_error
from Hand import Hand

full_house = Hand("TD TC TH 7C 7D".split())

with description('Given a hand with full house') as self:
  with context('When trying to rank the hand'):
    with it('should return 6'):
      expect(full_house.rank()).to(equal(6))