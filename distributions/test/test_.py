import pytest
import random
from distributions.draw import draw
from distributions.generator import NormalGen
from distributions.generator import PoissonGen
from distributions.generator import BinomialGen

# test function:

def test_draw_number_of_elements():
    n = draw(10, "normal", mu=0, sd=1)
    p = draw(100, "poisson", lam=1)
    b = draw(1000, "binomial", n=10, p=0.1)
    assert len(n) == 10
    assert len(p) == 100
    assert len(b) == 1000

def test_poisson_all_greater_than_or_equal_to_0():
    random.seed(0)
    p = draw(100, "poisson", lam=1)
    assert min(p) >= 0

def test_binomial_all_greater_than_or_equal_to_0():
    random.seed(0)
    p = draw(100, "binomial", n=10, p=0.1)
    assert min(p) >= 0


# test classes:

def test_normal_check_attributes():

    n = NormalGen(mu=10, sd=20)
    assert n.mu == 10
    assert n.sd == 20
    
def test_poisson_check_attributes():

    p = PoissonGen(lam=10)
    assert p.lam == 10

def test_binomial_check_attributes():

    b = BinomialGen(n=10, p=0.7)
    assert b.n == 10
    assert b.p == 0.7

def test_poisson_gen_all_greater_than_or_equal_to_0():
    b = PoissonGen(lam=10)
    samp = b.draw(100)
    assert min(samp) >= 0

def test_binomial_gen_all_greater_than_or_equal_to_0():
    b = BinomialGen(n=10, p = 0.7)
    samp = b.draw(100)
    assert min(samp) >= 0
