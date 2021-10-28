# Poker hands kata

The goal of this kata is to determine the best hand out of a set of hands
containing a set of poker cards (i.e. 5 cards).

This is a TDD version of the course [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212). The approach is outside-in, also known as the London school of TDD approach.

Refer also to [Test-Driven Development With Python: An Introduction to Mocking](https://medium.com/geekculture/test-driven-development-with-python-an-introduction-to-mocking-8ab6c1fe1c83).

# Implementation

In this section the implementation is described step-by-step.

## Behaviour on empty set of hands

We start by defining the behaviour for an empty set of hands.

```python
with description('Given an empty set of hands') as self:
  with context('When trying to rank the hands'):
    with it('should raise an exception'):
      expect(lambda: determine_best_hand([])) \
        .to(raise_error(IllegalArgumentsException))
```

This is implemented by

```python
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
```

## Behaviour on a set consisting of a single hand

```python
straight_flush = Hand("6C 7C 8C 9C T9".split())

with description('Given a set of one hand') as self:
  with context('When trying to rank the hands'):
    with it('should return the one and only hand'):
      hands = [straight_flush]
      expect(determine_best_hand(hands)).to(equal(straight_flush))
```

This is implemented by

```python
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
  elif len(hands) == 1:
    return hands[0]
```

and a Hand class

```python
class Hand:
  def __init__(self, cards):
    self.cards = cards
```

## Two equal hands

Let's assume two hands containing full house

```python
full_house = Hand("TD TC TH 7C 7D".split())

with description('Given full house versus full house') as self:
  with context('When trying to rank the hands'):
    with it('should return the full house hand'):
      hands = [full_house, full_house]
      expect(determine_best_hand(hands)).to(equal(full_house))
```

# Appendix

## Mamba example

The [example below](https://replit.com/@zwh/PokerHandsKata#mamba_dummy_spec.py) may be used as inspiration:
 
```python
from mamba import description, context, _context, it, _it, before, after
from expects import expect
from time import sleep
from mockito import when, mock
from doublex import Spy, assert_that, called, is_

class ASampleClass:
   pass

with description('mamba') as self:
  with it('is tested with mamba itself'):
    pass

  with it('supports python 3'):
    pass

  with context('when listing features'):
    with it('supports example groups'):
      pass

  with context('hooks'):
    with before.all:
      print ('This code will be run once, before all examples')

    with before.each:
      print ('This code will be run before each example')

    with after.each:
      print ('This code will be run after each example')

    with after.all:
      print ('This code will be run once, after all examples')

  with context('pending tests'):
    with _context('when running pending contexts (marked with a underscore)'):
      with it('will not run any spec under a pending context'):
        pass

  with _it('will not run pending specs (marked with underscore)'):
    pass

  with it('highlights slow tests'):
    sleep(10)

  with context(ASampleClass):
    with it('has an instance in subject property'):
      expect(self.subject).to.be.a(ASampleClass)

  with context('when writing assertions'):
    with it('can be used with plain assertions'):
      assert True

  with it('can be used with hamcrest style assertions'):
    assert_that(True, is_(True))

  with it('can be used with should_dsl style assertions'):
    True |should| be(True)

  with it('can be used with sure style assertions'):
    True.should.be.true

    expect(True).to.be.true

  with it('is assertion framework agnostic'):
    pass

  with context('when using tests doubles'):
    with it('can be used with mockito'):
      stub = mock()
      when(stub).is_usable_with_mockito().thenReturn(True)

      expect(stub.is_usable_with_mockito()).to.be.true

  with it('can be used with doublex'):
    with Spy() as sender:
      sender.is_usable_with_doublex().returns(True)

      assert_that(sender.is_usable_with_doublex(), is_(True))
      assert_that(sender.is_usable_with_doublex, called())

  with it('can be used with mock'):
    is_usable_with_mock = Mock(return_value=True)

    assert mock()

  with it('is test doubles framework agnostic'):
   pass

  with context('when code coverage measurement is desired'):
    with it('collects them if you pass `--enable-coverage`'):
      pass

  with it('calls `coverage` directly in order to compute it'):
    # see https://pypi.python.org/pypi/coverage/
    pass

  with it('is configured in a `.coveragerc` file at the root of your project'):
    # see http://nedbatchelder.com/code/coverage/config.html
    pass
```