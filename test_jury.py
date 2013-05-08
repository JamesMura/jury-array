from jury import Polynomial
from jury import Term
from jury import JuryArray
import pytest
def test_adding_two_terms():
    assert Term(2,3).add(Term(4,3)).p() == Term(6,3).p()

def test_you_cant_add_terms_of_different_powers():
    with pytest.raises(Exception):
        Term(1,2).add(Term(3,4))
def test_polynomial_print():
    a = Polynomial(Term(2,1),Term(3,2))
    assert a.p() == ' 3X2 2X1'

def test_polynomial_should_order_by_power():
    a = Polynomial(Term(2,1),Term(3,3),Term(2,2))
    assert a.p() == ' 3X3 2X2 2X1'

def test_polynomial_should_add_up_terms_with_same_power():
    a =Polynomial(Term(2,1),Term(3,1))
    assert a.p() == ' 5X1'
def test_generator():
    p = Polynomial(Term(1,4),Term(0.5,3),Term(0.3,2),Term(2,1),Term(2,0))
    array = JuryArray(p)
    for line in array.generate():
        print line

    assert False

