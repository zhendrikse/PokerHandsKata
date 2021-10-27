# Poker hands kata

TDD version of the course [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212).

Refer also to [Test-Driven Development With Python: An Introduction to Mocking](https://medium.com/geekculture/test-driven-development-with-python-an-introduction-to-mocking-8ab6c1fe1c83).

# Mamba example

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